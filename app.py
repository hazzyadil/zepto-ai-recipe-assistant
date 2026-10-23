import json
import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

st.title("Zepto AI Recipe Assistant")

if client is None:
    st.error("GROQ_API_KEY is missing. Add it to a .env file in the project folder.")

user_input = st.text_input("What do you want to cook or eat?")

if st.button("Get Recommendation", disabled=client is None):
    if not user_input.strip():
        st.warning("Enter a dish or ingredient before requesting a recommendation.")
    else:
        prompt = f"""You are a cooking assistant for a grocery app. The user wants: {user_input.strip()}. Respond with ONLY valid JSON, no other text, no explanations, no markdown. Format: {{"dish_name": "...", "ingredients": [{{"name": "...", "quantity": 0, "unit": "..."}}]}}"""

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
            )
        except Exception:
            st.error("Recipe generation failed. Check your API key and connection, then try again.")
        else:
            try:
                data = json.loads(response.choices[0].message.content)
                if not isinstance(data, dict):
                    raise ValueError("Expected a JSON object")

                dish_name = data.get("dish_name")
                ingredients = data.get("ingredients")

                if not isinstance(dish_name, str) or not dish_name.strip():
                    raise ValueError("Missing dish name")
                if not isinstance(ingredients, list) or not ingredients:
                    raise ValueError("Missing ingredients")
                for ingredient in ingredients:
                    if (
                        not isinstance(ingredient, dict)
                        or not isinstance(ingredient.get("name"), str)
                        or not ingredient["name"].strip()
                        or "quantity" not in ingredient
                        or not isinstance(ingredient.get("unit"), str)
                    ):
                        raise ValueError("Invalid ingredient")

            except (json.JSONDecodeError, TypeError, ValueError, IndexError):
                st.error("The recipe service returned an invalid response. Please try again.")
            else:
                st.session_state["dish_name"] = dish_name.strip()
                st.session_state["ingredients"] = ingredients

if "ingredients" in st.session_state:
    st.subheader(st.session_state["dish_name"])
    st.write("Check the ingredients you already have at home:")

    remaining_ingredients = []

    for index, ingredient in enumerate(st.session_state["ingredients"]):
        label = f"{ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}"
        is_checked = st.checkbox(label, key=f"ingredient-{index}-{ingredient['name']}")

        if not is_checked:
            remaining_ingredients.append(ingredient)

    if st.button("Add to Cart"):
        st.write("Adding to cart:")
        for ingredient in remaining_ingredients:
            st.write(f"- {ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}")
