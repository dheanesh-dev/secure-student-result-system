import json
import os

RESULTS_FILE = "data/results.json"


def load_results():
    if not os.path.exists(RESULTS_FILE) or os.path.getsize(RESULTS_FILE) == 0:
        return {}
    with open(RESULTS_FILE, "r") as f:
        return json.load(f)


def save_results(results):
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student():
    results = load_results()
    print("\n=== ADD STUDENT ===")

    student_id = input("Student ID: ").strip()
    if student_id in results:
        print("❌ Student already exists")
        return

    name = input("Student Name: ").strip()
    results[student_id] = {
        "name": name,
        "marks": {},
        "percentage": 0,
        "grade": "-"
    }

    save_results(results)
    print("✅ Student added successfully")


def add_or_update_marks():
    results = load_results()
    print("\n=== ADD / UPDATE MARKS ===")

    student_id = input("Student ID: ").strip()
    if student_id not in results:
        print("❌ Student not found")
        return

    subjects = ["Maths", "Science", "English"]
    total = 0

    for sub in subjects:
        try:
            mark = int(input(f"{sub} marks (0-100): "))
            if mark < 0 or mark > 100:
                raise ValueError
            results[student_id]["marks"][sub] = mark
            total += mark
        except ValueError:
            print("❌ Invalid mark")
            return

    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    results[student_id]["percentage"] = percentage
    results[student_id]["grade"] = grade

    save_results(results)
    print("✅ Marks updated successfully")


def view_students():
    results = load_results()
    print("\n=== STUDENT LIST ===")

    if not results:
        print("⚠️ No students found")
        return

    for sid, data in results.items():
        print(f"""
ID: {sid}
Name: {data['name']}
Marks: {data['marks']}
Percentage: {data['percentage']}
Grade: {data['grade']}
-------------------------
""")
