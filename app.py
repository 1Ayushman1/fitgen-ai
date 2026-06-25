import streamlit as st

from recommendation_engine import generate_plan
from pdf_generator import generate_pdf
from save_user import save_user


st.set_page_config(
    page_title="FITGEN AI",
    layout="wide"
)


st.title("🏋️ FITGEN AI")

st.subheader(
    "Personalized Workout & Diet Planner"
)


# -------------------
# INPUTS
# -------------------


col1,col2=st.columns(2)


with col1:

    name=st.text_input(
        "Name"
    )

    age=st.number_input(
        "Age",
        10,
        100,
        21
    )

    height=st.number_input(
        "Height (cm)",
        100,
        250,
        170
    )


with col2:

    weight=st.number_input(
        "Weight (kg)",
        30,
        200,
        70
    )

    goal=st.selectbox(

        "Goal",

        [

        "Weight Loss",

        "Muscle Gain",

        "Maintain"

        ]

    )



food=st.selectbox(

"Food Preference",

[
"Veg",
"NonVeg"
]

)



budget=st.selectbox(

"Budget",

[
"Low",
"Medium",
"High"
]

)






experience=st.selectbox(

"Workout Experience",

[
"Beginner",

"Intermediate",

"Advanced"

]

)



activity=st.selectbox(

"Activity Level",

[
"Sedentary",

"Moderate",

"Active"

]

)



location=st.selectbox(

"Workout Location",

[
"Home",

"Gym"

]

)



allergy=st.text_input(
"Food Allergy"
)



# -------------------
# BUTTONS
# -------------------


c1,c2=st.columns(2)


with c1:

    save=st.button(
        "💾 Save User Details"
    )


with c2:

    generate=st.button(
        "Generate Professional Plan"
    )



# -------------------
# SAVE
# -------------------


if st.button("💾 Save User Details"):

    save_user(

        name,

        age,

        goal,

        result["bmi"],

        result["category"],

        result["calories"]

    )

    st.success(
        "User Saved Successfully"
    )


# -------------------
# GENERATE
# -------------------


if generate:


    result=generate_plan(

        age,

        height,

        weight,

        goal,

        budget,

        food,

        experience,

        activity,

        allergy

    )



    st.header(
        "📊 Health Dashboard"
    )


    a,b,c,d=st.columns(4)



    a.metric(
        "BMI",
        result["bmi"]
    )


    b.metric(
        "Category",
        result["category"]
    )


    c.metric(
        "Calories",
        str(result["calories"])
        +
        " kcal"
    )


    d.metric(
        "Water",
        str(result["water"])
        +
        " L"
    )



    st.warning(

f"""

⭐ Recovery Recommendation


Sleep:

{result["sleep"]}


Water:

{result["water"]} L


Rest:

Sunday

"""

    )




# WORKOUT


    st.header(
        "🏋️ Weekly Workout"
    )


    for day in result["workout"]:


        with st.expander(day):


            st.write(

                result["workout"][day]

            )



# DIET


    st.header(
        "🍛 Diet Plan"
    )


    for meal in result["diet"]:


        with st.expander(meal):


            st.write(

                result["diet"][meal]

            )



# PDF


    pdf=generate_pdf(

        name,

        result

    )



    with open(
        pdf,
        "rb"
    ) as f:


        st.download_button(

            "📄 Download Premium Report",

            f,

            file_name=pdf

        )



    st.success(
        "Plan generated successfully."
    )


    st.info(
        "Generate report anytime without saving."
    )
