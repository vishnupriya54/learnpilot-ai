import json

def load_courses():
    with open("courses.json", "r") as f:
        return json.load(f)

def calculate_progress(known_skills, roadmap):
    total = len(roadmap)
    completed = len(known_skills)

    if total == 0:
        return 0

    return min(int((completed / total) * 100), 100)