
disease_food_dict = {
    "diabetes": ["Leafy greens", "Whole grains", "Nuts", "Berries", "Fish"],
    "hypertension": ["Leafy greens", "Berries", "Red beets", "Oatmeal", "Bananas"],
    "anemia": ["Red meat", "Poultry", "Seafood", "Beans", "Dark leafy greens"],
    "osteoporosis": ["Dairy products", "Leafy greens", "Fish", "Nuts", "Tofu"],
    "constipation": ["Whole grains", "Fruits", "Vegetables", "Nuts", "Seeds"],
    "acid reflux": ["Bananas", "Melons", "Oatmeal", "Green vegetables", "Lean poultry"],
}


print("Welcome to the Food Recommendation System!")
print("Enter a disease to get food recommendations.\n")


user_disease = input("Please enter a disease: ").strip().lower()


if user_disease in disease_food_dict:
    recommended_foods = disease_food_dict[user_disease]
    print(f"\nFor {user_disease}, you should consider eating the following foods:")
    for food in recommended_foods:
        print(f"- {food}")
else:
    print("\nSorry, we don't have food recommendations for that disease at the moment.")

print("\nStay healthy and take care!")
