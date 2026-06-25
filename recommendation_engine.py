def get_food_plan(goal, preference):

    if preference == "Non-Veg":

        protein = "Chicken / Eggs"

    else:

        protein = "Paneer"

    if goal == "Muscle Gain":

        return {

            "Breakfast":
            f"4 Eggs if Non-Veg else Paneer + Milk + Banana",

            "Lunch":
            f"Rice + {protein} + Dal + Vegetables",

            "Snacks":
            "Milk + Peanut Butter + Banana Shake",

            "Dinner":
            f"Roti + {protein} + Vegetables"

        }

    elif goal == "Weight Loss":

        return {

            "Breakfast":
            f"Eggs/Oats if Non-Veg else Paneer/Oats",

            "Lunch":
            f"2 Roti + {protein} + Salad",

            "Snacks":
            "Fruit + Green Tea",

            "Dinner":
            f"{protein} + Vegetables"

        }

    else:

        return {

            "Breakfast":
            f"Eggs/Bread if Non-Veg else Paneer/Bread",

            "Lunch":
            f"Rice + {protein}",

            "Snacks":
            "Fruit + Nuts",

            "Dinner":
            f"Roti + {protein}"

        }
