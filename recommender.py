import json

def load_courses():
    with open("courses.json", "r") as f:
        return json.load(f)

def get_course_catalog():

    courses = load_courses()

    catalog = ""

    for course in courses:

        description = course.get(
            "description",
            "No description available."
        )

        catalog += f"""
Course : {course['name']}
Difficulty : {course['difficulty']}
Duration : {course['duration']}
Prerequisites : {course['prerequisites']}
Description : {description}

"""

    return catalog