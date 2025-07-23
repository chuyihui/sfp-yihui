import streamlit as st
import random
import time

# Extended food database with 28 total items now (8 original + 20 new)
foods = [
    {"emoji": "🍕", "name": "Pizza", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 285, "Protein": "12g", "Carbs": "36g", "Fat": "10g"}},
    {"emoji": "🍣", "name": "Sushi", "category": "Asian", "vegetarian": False, "low_carb": True, "high_protein": True,
     "nutrition": {"Calories": 200, "Protein": "12g", "Carbs": "28g", "Fat": "3g"}},
    {"emoji": "🥗", "name": "Salad", "category": "Western", "vegetarian": True, "low_carb": True, "high_protein": False,
     "nutrition": {"Calories": 150, "Protein": "3g", "Carbs": "10g", "Fat": "10g"}},
    {"emoji": "🍜", "name": "Ramen", "category": "Asian", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 430, "Protein": "20g", "Carbs": "50g", "Fat": "15g"}},
    {"emoji": "🍛", "name": "Curry", "category": "Asian", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 350, "Protein": "15g", "Carbs": "40g", "Fat": "12g"}},
    {"emoji": "🥩", "name": "Steak", "category": "Western", "vegetarian": False, "low_carb": True, "high_protein": True,
     "nutrition": {"Calories": 679, "Protein": "62g", "Carbs": "0g", "Fat": "48g"}},
    {"emoji": "🍚", "name": "Fried Rice", "category": "Asian", "vegetarian": False, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 333, "Protein": "7g", "Carbs": "45g", "Fat": "10g"}},
    {"emoji": "🍇", "name": "Fruit Bowl", "category": "Other", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 120, "Protein": "1g", "Carbs": "30g", "Fat": "0g"}},
    
    # 20 new food items added:
    {"emoji": "🌮", "name": "Tacos", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 170, "Protein": "9g", "Carbs": "18g", "Fat": "8g"}},
    {"emoji": "🥟", "name": "Dumplings", "category": "Asian", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 220, "Protein": "9g", "Carbs": "26g", "Fat": "7g"}},
    {"emoji": "🥪", "name": "Club Sandwich", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 400, "Protein": "20g", "Carbs": "35g", "Fat": "18g"}},
    {"emoji": "🥞", "name": "Pancakes", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 175, "Protein": "6g", "Carbs": "28g", "Fat": "5g"}},
    {"emoji": "🥩", "name": "Grilled Chicken", "category": "Western", "vegetarian": False, "low_carb": True, "high_protein": True,
     "nutrition": {"Calories": 250, "Protein": "30g", "Carbs": "0g", "Fat": "6g"}},
    {"emoji": "🍤", "name": "Tempura", "category": "Asian", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 300, "Protein": "18g", "Carbs": "20g", "Fat": "15g"}},
    {"emoji": "🍞", "name": "Sandwich", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 250, "Protein": "12g", "Carbs": "30g", "Fat": "6g"}},
    {"emoji": "🍟", "name": "Fries", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 365, "Protein": "3.4g", "Carbs": "48g", "Fat": "17g"}},
    {"emoji": "🌭", "name": "Hot Dog", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 290, "Protein": "10g", "Carbs": "27g", "Fat": "17g"}},
    {"emoji": "🧀", "name": "Mac & Cheese", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 310, "Protein": "12g", "Carbs": "30g", "Fat": "15g"}},
    {"emoji": "🍩", "name": "Donut", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 195, "Protein": "2g", "Carbs": "22g", "Fat": "11g"}},
    {"emoji": "🍪", "name": "Cookie", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 160, "Protein": "2g", "Carbs": "22g", "Fat": "7g"}},
    {"emoji": "🍦", "name": "Ice Cream", "category": "Western", "vegetarian": True, "low_carb": False, "high_protein": False,
     "nutrition": {"Calories": 207, "Protein": "4g", "Carbs": "24g", "Fat": "11g"}},
    {"emoji": "🍗", "name": "Fried Chicken", "category": "Western", "vegetarian": False, "low_carb": True, "high_protein": True,
     "nutrition": {"Calories": 320, "Protein": "25g", "Carbs": "8g", "Fat": "20g"}},
    {"emoji": "🥘", "name": "Paella", "category": "Western", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 350, "Protein": "18g", "Carbs": "40g", "Fat": "8g"}},
    {"emoji": "🥗", "name": "Quinoa Salad", "category": "Western", "vegetarian": True, "low_carb": True, "high_protein": True,
     "nutrition": {"Calories": 220, "Protein": "8g", "Carbs": "30g", "Fat": "6g"}},
    {"emoji": "🍲", "name": "Pho", "category": "Asian", "vegetarian": False, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 350, "Protein": "20g", "Carbs": "45g", "Fat": "10g"}},
    {"emoji": "🥙", "name": "Falafel Wrap", "category": "Other", "vegetarian": True, "low_carb": False, "high_protein": True,
     "nutrition": {"Calories": 320, "Protein": "12g", "Carbs": "35g", "Fat": "10g"}},
]

# Initialize session state
if 'remaining_foods' not in st.session_state:
    st.session_state.remaining_foods = foods.copy()
    st.session_state.selected_food = None

st.title("🥗 Food Thinker App")
st.markdown("Can't decide what to eat? Let this app suggest something based on your tastes!")

# --- Search filters ---
st.sidebar.header("🔍 Customize Your Preferences")

category = st.sidebar.selectbox("Cuisine Type", ["Any", "Asian", "Western", "Other"])
vegetarian = st.sidebar.checkbox("Vegetarian")
low_carb = st.sidebar.checkbox("Low-Carb")
high_protein = st.sidebar.checkbox("High-Protein")

# Filter foods based on preferences
def food_matches(f):
    return (
        (category == "Any" or f["category"] == category) and
        (not vegetarian or f["vegetarian"]) and
        (not low_carb or f["low_carb"]) and
        (not high_protein or f["high_protein"])
    )

filtered_foods = [f for f in st.session_state.remaining_foods if food_matches(f)]

with st.expander("📋 Matching Food Options"):
    if filtered_foods:
        st.write([f"{f['emoji']} {f['name']}" for f in filtered_foods])
    else:
        st.write("No foods match your filters. Try adjusting your preferences.")

# Pick food
if st.button("🎲 Think for me!"):
    if filtered_foods:
        with st.spinner("🤔 Thinking..."):
            time.sleep(1.5)
        choice = random.choice(filtered_foods)
        st.session_state.selected_food = choice
        st.session_state.remaining_foods.remove(choice)
    else:
        st.warning("🚫 No matching food found. Reset or change filters.")

# Show result
if st.session_state.selected_food:
    food = st.session_state.selected_food
    st.success(f"🥳 You should eat: **{food['emoji']} {food['name']}**")
    st.markdown("### 🍽️ Nutrition Facts (per serving)")
    n = food["nutrition"]
    st.markdown(f"- **Calories**: {n['Calories']} kcal\n- **Protein**: {n['Protein']}\n- **Carbs**: {n['Carbs']}\n- **Fat**: {n['Fat']}")
    
    # Reasoning
    reason = []
    if vegetarian and food["vegetarian"]: reason.append("it's vegetarian")
    if low_carb and food["low_carb"]: reason.append("it's low in carbs")
    if high_protein and food["high_protein"]: reason.append("it's high in protein")
    if reason:
        st.info(f"✅ This food was suggested because {', and '.join(reason)}.")
    else:
        st.info("Suggested based on your selected cuisine type.")

# Reset button
if st.button("🔄 Reset"):
    st.session_state.remaining_foods = foods.copy()
    st.session_state.selected_food = None
