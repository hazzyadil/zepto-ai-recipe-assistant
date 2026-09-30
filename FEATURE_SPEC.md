Zepto AI Recipe Assistant — Feature Spec

1. Problem

Users who want to cook a dish often need to get a recipe and ingredient list from one source, then manually search for each ingredient in a grocery app and add them to their cart. This creates unnecessary time and effort.

The Zepto AI Recipe Assistant reduces this friction by turning a user’s cooking goal into a structured recipe and ingredient list, then helping them identify which ingredients they still need to buy.

2. User Flow

Input → Recommendation → Pantry Check → Shopping List

1. User enters a cooking goal, such as “high-protein dinner.”
2. User clicks Get Recommendation.
3. The LLM generates one suitable dish and its ingredients with quantities.
4. Each ingredient appears with a checkbox.
5. User checks the ingredients they already have at home.
6. The app identifies the unchecked ingredients as the items they still need.
7. User clicks Add to Cart to display the remaining ingredients.

3. LLM Integration

The LLM is called when the user clicks Get Recommendation.

* Provider: Groq API
* Model: openai/gpt-oss-20b
* Input: User’s free-text cooking goal
* Output: Structured JSON containing:
    * dish_name
    * ingredients
    * ingredient name
    * quantity
    * unit

The application parses the JSON response and stores the dish and ingredients in Streamlit session state so checkbox interactions don’t trigger additional LLM calls.

4. Fallback / Error Handling

The current prototype has limited error handling. If the LLM returns an invalid or empty JSON response, json.loads() can raise a JSONDecodeError.

Future behavior: catch API and JSON parsing errors and show a user-friendly retry message instead of allowing the application to crash.

5. Success Metrics

The feature can be evaluated using:

* Time saved: Time required to go from cooking goal to a usable shopping list compared with the manual workflow.
* Steps reduced: Number of manual recipe searches and ingredient searches/cart actions avoided.
* Completion rate: Percentage of users who enter a cooking goal and successfully reach their final ingredient list.

Current Prototype Scope

The current prototype does not directly add items to a real Zepto cart. The Add to Cart action currently displays the ingredients the user still needs. Real grocery-cart integration would be a future development step.