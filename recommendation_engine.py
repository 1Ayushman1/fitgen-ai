from workout_library import (
    muscle_gain,
    weight_loss,
    maintain
)

from diet_library import (
    diet
)



def calculate_sleep(
age,
goal
):

    if age<=18:

        return "8.5–10 hrs"


    elif age<=25:

        if goal=="Muscle Gain":

            return "8–9 hrs"

        elif goal=="Weight Loss":

            return "7.5–8.5 hrs"

        else:

            return "7–8 hrs"


    elif age<=45:

        return "7–8 hrs"


    else:

        return "7 hrs"




def calculate_water(
weight
):

    return round(
        weight*0.04,
        1
    )




def calculate_calories(
age,
height,
weight,
goal,
activity
):

    bmr=(

10*weight

+

6.25*height

-

5*age

+

5

    )


    if activity=="Sedentary":

        calories=bmr*1.2


    elif activity=="Moderate":

        calories=bmr*1.45


    else:

        calories=bmr*1.7



    if goal=="Muscle Gain":

        calories+=300


    elif goal=="Weight Loss":

        calories-=350



    return int(
        calories
    )





def get_bmi(
height,
weight
):

    bmi=round(

weight/

((height/100)**2),

2

    )


    if bmi<18.5:

        category="Underweight"

    elif bmi<25:

        category="Normal"

    elif bmi<30:

        category="Overweight"

    else:

        category="Obese"


    return bmi,category





def modify_for_food(
meal,
food
):

    if food=="Veg":

        meal=meal.replace(
            "Chicken",
            "Paneer"
        )

        meal=meal.replace(
            "Eggs",
            "Paneer"
        )

        meal=meal.replace(
            "eggs",
            "Paneer"
        )

    return meal





def remove_allergy(
meal,
allergy
):

    if allergy.strip():

        meal=meal.replace(
            allergy,
            "[REMOVED]"
        )

    return meal





def budget_adjust(
meal,
budget
):

    if budget=="Low":

        meal+="\n\nBudget Tip:\nUse local affordable options."


    elif budget=="Medium":

        meal+="\n\nBudget Tip:\nBalanced quality."


    else:

        meal+="\n\nBudget Tip:\nPremium quality allowed."


    return meal





def generate_plan(

age,

height,

weight,

goal,

budget,

food,

experience,

activity,

allergy

):


# WORKOUT


    if goal=="Muscle Gain":

        workout=muscle_gain


    elif goal=="Weight Loss":

        workout=weight_loss


    else:

        workout=maintain




# DIET


    meal=diet[
goal
]



    for key in meal:

        meal[key]=modify_for_food(
meal[key],
food
        )

        meal[key]=remove_allergy(
meal[key],
allergy
        )

        meal[key]=budget_adjust(
meal[key],
budget
        )



    calories=calculate_calories(

age,

height,

weight,

goal,

activity

    )


    water=calculate_water(
weight
    )


    sleep=calculate_sleep(

age,

goal

    )


    bmi,category=get_bmi(

height,

weight

    )



    return {

"calories":calories,

"water":water,

"sleep":sleep,

"workout":workout,

"diet":meal,

"bmi":bmi,

"category":category

}
