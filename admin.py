import json
import os

RESULTS_FILE = "data/results.json"
USERS_FILE = "data/users.json"


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        return json.load(f)


def save_results(results):
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def add_student():
    users = load_users()
    results = load_results()

    roll_no = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    password = input("Create Password: ")

    # Check if student already exists
    for user in users:
        if user["roll_no"] == roll_no:
            print("❌ Student already exists!")
            return

    users.append({
        "roll_no": roll_no,
        "name": name,
        "password": password,
        "role": "student"
    })

    results.append({
        "roll_no": roll_no,
        "name": name,
        "marks": {}
    })

    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

    save_results(results)

    print("✅ Student added successfully!")


def update_marks():
    results = load_results()
    roll_no = input("Enter Roll No: ")

    for student in results:
        if student["roll_no"] == roll_no:
            student["marks"]["Maths"] = int(input("Maths: "))
            student["marks"]["Science"] = int(input("Science: "))
            student["marks"]["English"] = int(input("English: "))

            save_results(results)
            print("✅ Marks updated successfully!")
            return

    print("❌ Student not found!")


def view_all_results():
    results = load_results()

    if not results:
        print("No student records found.")
        return

    for student in results:
        print("\n-----------------------")
        print("Roll No :", student["roll_no"])
        print("Name    :", student["name"])
        print("Marks   :", student["marks"])
