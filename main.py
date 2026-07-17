import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from recommender import recommend_courses
from prompt import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


# Load student profiles
with open("sample_profiles.json", "r") as file:
    students = json.load(file)


print("\n===== Course Recommendation Agent =====\n")

print("Available Students:")

for student in students:
    print("-", student["name"])

name = input("\nEnter Student Name: ")

selected = None

for student in students:
    if student["name"].lower() == name.lower():
        selected = student
        break

if selected is None:
    print("Student not found!")
    exit()

recommended = recommend_courses(selected)

course_names = [course["name"] for course in recommended]

prompt = f"""
{SYSTEM_PROMPT}

Student Profile

Name: {selected['name']}

Background: {selected['background']}

Career Goal: {selected['goal']}

Known Skills:
{selected['known_skills']}

Recommended Learning Path:
{course_names}

Explain why each course should be learned in this order.
"""

response = model.generate_content(prompt)

print("\n==============================")
print("Recommended Learning Path")
print("==============================\n")

for i, course in enumerate(course_names, start=1):
    print(f"{i}. {course}")

print("\n==============================")
print("AI Explanation")
print("==============================\n")

print(response.text)