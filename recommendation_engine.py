# recommendation_engine.py


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    return "Obese"


def calculate_water(weight):

    return round(weight * 0.035, 1)


def sleep_hours(age, goal):

    if age <= 18:
        return "8–10 hrs"

    if goal == "Muscle Gain":
        return "8–9 hrs"

    return "7–8 hrs"


def calories(weight, height, age, gender, goal):

    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    if goal == "Muscle Gain":
        bmr += 350

    elif goal == "Weight Loss":
        bmr -= 400

    return int(bmr)


def get_food_plan(goal, preference):

    nonveg = preference == "Non-Veg"

    protein = (
        "Chicken + Eggs"
        if nonveg
        else "Paneer"
    )

    if goal == "Muscle Gain":

        return {

            "Breakfast":
            (
                "4 Eggs + Oats + Milk + Banana"
                if nonveg
                else
                "Paneer + Oats + Milk + Banana"
            ),

            "Lunch":
            f"Rice + {protein} + Dal + Vegetables + Curd",

            "Snacks":
            (
                "Milk Shake + Peanut Butter Sandwich"
                if nonveg
                else
                "Banana Shake + Nuts"
            ),

            "Dinner":
            f"Roti + {protein} + Vegetables"

        }

    elif goal == "Weight Loss":

        return {

            "Breakfast":
            (
                "2 Eggs + Oats"
                if nonveg
                else
                "Paneer + Oats"
            ),

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
            (
                "Eggs + Bread + Fruit"
                if nonveg
                else
                "Paneer + Bread + Fruit"
            ),

            "Lunch":
            f"Rice + {protein}",

            "Snacks":
            "Fruit + Nuts",

            "Dinner":
            f"Roti + {protein}"

        }


def workout_plan(goal):

    if goal == "Muscle Gain":

        return {

            "Monday":
            "Chest + Triceps",

            "Tuesday":
            "Back + Biceps",

            "Wednesday":
            "Leg Day",

            "Thursday":
            "Shoulders + Abs",

            "Friday":
            "Upper Strength",

            "Saturday":
            "Full Body",

            "Sunday":
            "Recovery"

        }

    elif goal == "Weight Loss":

        return {

            "Monday":
            "Chest + Cardio",

            "Tuesday":
            "Back + Walking",

            "Wednesday":
            "Legs + Core",

            "Thursday":
            "Active Recovery",

            "Friday":
            "Shoulders + Cardio",

            "Saturday":
            "Fat Loss Circuit",

            "Sunday":
            "Recovery"

        }

    else:

        return {

            "Monday":
            "Upper Body",

            "Tuesday":
            "Lower Body",

            "Wednesday":
            "Cardio + Core",

            "Thursday":
            "Pull",

            "Friday":
            "Full Body",

            "Saturday":
            "Lifestyle Activity",

            "Sunday":
            "Recovery"

        }


def generate_plan(
        age,
        gender,
        weight,
        height,
        goal,
        preference,
        budget
):

    bmi = round(
        weight /
        (
            (height / 100) ** 2
        ),
        2
    )

    return {

        "bmi":
        bmi,

        "category":
        bmi_category(bmi),

        "calories":
        calories(
            weight,
            height,
            age,
            gender,
            goal
        ),

        "water":
        calculate_water(weight),

        "sleep":
        sleep_hours(
            age,
            goal
        ),

        "goal":
        goal,

        "budget":
        budget,

        "diet":
        get_food_plan(
            goal,
            preference
        ),

        "workout":
        workout_plan(
            goal
        )

    }
