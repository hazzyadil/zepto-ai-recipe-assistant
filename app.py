import streamlit as st
import json
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Zepto AI Recipe Assistant")

user_input = st.text_input("What do you want to cook or eat?")

if st.button("Get Recommendation"):
    prompt = f"""You are a cooking assistant for a grocery app. The user wants: {user_input}. Respond with ONLY valid JSON, no other text, no explanations, no markdown. Format: {{"dish_name": "...", "ingredients": [{{"name": "...", "quantity": 0, "unit": "..."}}]}}"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    data = json.loads(response.choices[0].message.content)

    st.session_state["dish_name"] = data["dish_name"]
    st.session_state["ingredients"] = data["ingredients"]

if "ingredients" in st.session_state:
    st.subheader(st.session_state["dish_name"])
    st.write("Check the ingredients you already have at home:")

    remaining_ingredients = []

    for ingredient in st.session_state["ingredients"]:
        label = f"{ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}"
        is_checked = st.checkbox(label, key=ingredient['name'])

        if not is_checked:
            remaining_ingredients.append(ingredient)

    if st.button("Add to Cart"):
        st.write("Adding to cart:")
        for ingredient in remaining_ingredients:
            st.write(f"- {ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}")
