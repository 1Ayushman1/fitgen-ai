from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer,
Table,
TableStyle,
Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch



def generate_pdf(
name,
result
):

    file="FITGEN_REPORT.pdf"

    doc=SimpleDocTemplate(
        file,
        leftMargin=30,
        rightMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles=getSampleStyleSheet()

    story=[]





# --------------------------------
# HEADER
# --------------------------------


    header=Table(

[
[
"FITGEN AI\nProfessional Workout & Diet Report"
]
],

colWidths=520

    )


    header.setStyle(

TableStyle([

(
"BACKGROUND",
(0,0),
(-1,-1),
colors.darkblue
),

(
"TEXTCOLOR",
(0,0),
(-1,-1),
colors.white
),

(
"BOX",
(0,0),
(-1,-1),
3,
colors.black
),

(
"FONTSIZE",
(0,0),
(-1,-1),
22
),

(
"PADDING",
(0,0),
(-1,-1),
18
)

])

    )


    story.append(header)

    story.append(
Spacer(
1,
25
)
    )



# --------------------------------
# PROFILE
# --------------------------------


    story.append(

Paragraph(

"<b>USER PROFILE</b>",

styles[
"Heading1"
]

)

    )


    profile=[

[
"Name",
name
],

[
"BMI",
str(
result[
"bmi"
]
)
],

[
"Category",
result[
"category"
]
],

[
"Calories",
str(
result[
"calories"
]
)
+
" kcal/day"
],

[
"Recommended Sleep",
result[
"sleep"
]
],

[
"Water",
str(
result[
"water"
]
)
+
" L/day"
]

]


    t=Table(

profile,

colWidths=[
180,
320
]

    )


    t.setStyle(

TableStyle([

(
"GRID",
(0,0),
(-1,-1),
2,
colors.black
),

(
"BACKGROUND",
(0,0),
(0,-1),
colors.lightblue
),

(
"PADDING",
(0,0),
(-1,-1),
12
)

])

    )


    story.append(t)

    story.append(
Spacer(
1,
25
)
)



# --------------------------------
# DAYWISE WORKOUT
# --------------------------------


    story.append(

Paragraph(

"<b>🏆 DAY-WISE FITNESS PLAN</b>",

styles[
"Heading1"
]

)

    )



    for day in result[
"workout"
]:


        rows=[

[
day
],

[
result[
"workout"
][
day
]
]

        ]


        workout_table=Table(

rows,

colWidths=[
500
]

        )


        workout_table.setStyle(

TableStyle([

(
"GRID",
(0,0),
(-1,-1),
2,
colors.black
),

(
"BACKGROUND",
(0,0),
(-1,0),
colors.lightgrey
),

(
"PADDING",
(0,0),
(-1,-1),
12
)

])

        )


        story.append(
workout_table
        )


# --------------------------------
# DIET
# --------------------------------


        meal_rows=[]


        for meal in result[
"diet"
]:

            meal_rows.append(

[
meal,

result[
"diet"
][
meal
]

]

            )



        diet_table=Table(

meal_rows,

colWidths=[
140,
360
]

        )


        diet_table.setStyle(

TableStyle([

(
"GRID",
(0,0),
(-1,-1),
2,
colors.black
),

(
"BACKGROUND",
(0,0),
(0,-1),
colors.lightyellow
),

(
"PADDING",
(0,0),
(-1,-1),
12
)

])

        )


        story.append(
diet_table
        )

        story.append(
Spacer(
1,
20
)
        )




# --------------------------------
# RECOVERY
# --------------------------------


    story.append(

Paragraph(

"<b>⭐ MANDATORY RECOVERY</b>",

styles[
"Heading1"
]

)

    )



    recovery=[

[
"Sleep",
result[
"sleep"
]
],

[
"Water",
str(
result[
"water"
]
)
+
" L"
],

[
"Rest Day",
"Sunday"
]

]


    r=Table(

recovery,

colWidths=[
180,
320
]

    )


    r.setStyle(

TableStyle([

(
"GRID",
(0,0),
(-1,-1),
2,
colors.black
),

(
"BACKGROUND",
(0,0),
(0,-1),
colors.orange
),

(
"PADDING",
(0,0),
(-1,-1),
12
)

])

    )


    story.append(r)

    story.append(
Spacer(
1,
25
)
)



# --------------------------------
# FOOTER
# --------------------------------


    story.append(

Paragraph(

"""
Powered by FITGEN AI

Train Smart • Recover Smart • Grow Smart
""",

styles[
"Normal"
]

)

    )



    doc.build(
story
    )



    return file
