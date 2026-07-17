import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

from recommender import get_course_catalog
from prompt import SYSTEM_PROMPT


# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="LearnPilot AI",
    page_icon="🚀",
    layout="wide"
)


# -------------------------
# Load Gemini API
# -------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Add it in your .env file")
    st.stop()


genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



# -------------------------
# Custom CSS
# -------------------------

st.markdown("""
<style>

.stApp{
background: radial-gradient(circle at top,#1E3A8A,#0F172A,#020617);
color:white;
}


section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#020617,#111827,#1E293B);
}


section[data-testid="stSidebar"] *{
color:white !important;
}


label{
color:white !important;
font-weight:700 !important;
}


.stTextInput input,
textarea,
.stSelectbox div[data-baseweb="select"]{
background:white !important;
color:black !important;
}


.stButton>button{

background:linear-gradient(
90deg,
#2563EB,
#7C3AED
);

height:60px;
font-size:20px;
font-weight:bold;
border-radius:15px;
width:100%;
color:white;

}


.stButton>button:hover{

background:linear-gradient(
90deg,
#1D4ED8,
#6D28D9
);

}


div[data-testid="metric-container"]{

background:#172554;
border-radius:18px;
padding:15px;
color:white;

}

</style>

""",
unsafe_allow_html=True)



# -------------------------
# Header
# -------------------------


st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#7C3AED);
padding:45px;
border-radius:20px;
text-align:center;
color:white;
">

<h1 style="font-size:55px;">
🚀 LearnPilot AI
</h1>

<h3>
Your Personal AI Learning Mentor
</h3>


<p style="font-size:20px">

Generate personalized learning roadmaps
using Google Gemini AI.

</p>


</div>

""",
unsafe_allow_html=True)



# Feature Cards

c1,c2,c3,c4 = st.columns(4)


c1.info("🎯 Personalized Roadmaps")

c2.info("🤖 Gemini AI")

c3.info("📚 Smart Course Ordering")

c4.info("📄 Download Report")



# -------------------------
# Sidebar
# -------------------------


st.sidebar.image(
"https://img.icons8.com/color/96/artificial-intelligence.png",
width=80
)


st.sidebar.title(
"🚀 LearnPilot AI"
)


st.sidebar.subheader(
"🧠 AI Learning Mentor"
)


st.sidebar.write("""

Get personalized learning roadmap based on:

✔ Academic Background

✔ Career Goal

✔ Current Skills

""")


st.sidebar.subheader(
"✨ Features"
)


st.sidebar.write("""

📚 Smart Course Recommendations

🤖 Gemini AI Explanation

🛣 Personalized Roadmap

📈 Progress Tracking

⬇ Download Report

""")


# Metrics

st.sidebar.markdown("---")

st.sidebar.metric(
"Students",
"5K+"
)

st.sidebar.metric(
"Courses",
"120+"
)

st.sidebar.metric(
"Response",
"3 sec"
)




# -------------------------
# Career Options
# -------------------------


career_options={


"B.Tech CSE":[

"Software Developer",
"Full Stack Developer",
"Backend Developer",
"Java Developer",
"Python Developer",
"Generative AI Engineer",
"Machine Learning Engineer",
"Data Scientist",
"Cloud Engineer",
"DevOps Engineer",
"AI Engineer"

],


"ECE":[

"Embedded Systems Engineer",
"VLSI Engineer",
"IoT Engineer",
"Software Developer",
"AI Engineer"

],


"Mechanical":[

"Mechanical Design Engineer",
"CAD Engineer",
"Robotics Engineer",
"Data Analyst"

],


"BCA":[

"Software Developer",
"Python Developer",
"Full Stack Developer",
"Cloud Engineer",
"Generative AI Engineer"

],


"Other":[

"Software Developer",
"AI Engineer",
"Cloud Engineer"

]


}



# -------------------------
# Student Profile
# -------------------------


st.markdown(
"""
<h1 style="color:white">
👤 Student Profile
</h1>
""",
unsafe_allow_html=True
)



col1,col2=st.columns(2)



with col1:


    name=st.text_input(
    "Student Name"
    )


    background=st.selectbox(

    "Background",

    list(career_options.keys())

    )



with col2:


    goal=st.selectbox(

    "Career Goal",

    career_options[background]

    )


    skills=st.text_area(

    "Known Skills (comma separated)",

    "Python Basics"

    )





# -------------------------
# Generate Roadmap
# -------------------------


if st.button(
"🚀 Generate Learning Roadmap"
):


    student={

    "name":name,

    "background":background,

    "goal":goal,

    "known_skills":[
        x.strip()
        for x in skills.split(",")
    ]

    }



    course_catalog=get_course_catalog()



    prompt=f"""

{SYSTEM_PROMPT}


Student Profile

Name:
{name}


Background:
{background}


Career Goal:
{goal}


Skills:
{student['known_skills']}


Course Catalog:

{course_catalog}



Generate an ordered learning roadmap.


Include:


1. Course Name

2. Difficulty

3. Duration

4. Why selected

5. Career Benefit

6. Mini Project



Also include:

Estimated Learning Time

Final Career Advice

"""



    with st.spinner(
    "🧠 Gemini AI is creating roadmap..."
    ):


        try:


            response=model.generate_content(prompt)



            roadmap=response.text



        except Exception as e:


            st.error(
            f"Gemini Error: {e}"
            )

            st.stop()



    st.success(
    "✅ Recommendation Generated Successfully!"
    )


    st.balloons()



    st.markdown(
    "## 🎯 Personalized Learning Roadmap"
    )


    with st.container(border=True):


        st.markdown(
        roadmap
        )



        st.subheader(
        "📈 Learning Progress"
        )


        progress=min(
            len(student["known_skills"])/10,
            1
        )


        st.progress(progress)


        st.write(
        f"Current Progress : {int(progress*100)}%"
        )



        st.download_button(

        label="⬇ Download Recommendation",

        data=roadmap,

        file_name="LearnPilot_Roadmap.txt",

        mime="text/plain"

        )





# -------------------------
# Footer
# -------------------------


st.markdown(
"""

<center style="color:white">

🚀 LearnPilot AI | Powered by Google Gemini

</center>

""",
unsafe_allow_html=True
)