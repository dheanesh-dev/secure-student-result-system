import json
import os

RESULTS_FILE = "data/results.json"


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_results(results):
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


def add_result():
    results = load_results()

    username = input("Student Username: ").strip()
    roll = input("Student Roll No: ").strip()
    name = input("Student Name: ").strip()
    marks = int(input("Marks: "))

    results.append({
        "username": username,
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_results(results)
    print("✅ Result added successfully")


def update_result():
    results = load_results()
    roll = input("Enter Roll No to update: ").strip()

    for r in results:
        if r["roll"] == roll:
            r["marks"] = int(input("Enter new marks: "))
            save_results(results)
            print("✅ Result updated")
            return

    print("❌ Student not found")


def delete_result():
    results = load_results()
    roll = input("Enter Roll No to delete: ").strip()

    new_results = [r for r in results if r["roll"] != roll]

    if len(new_results) == len(results):
        print("❌ Student not found")
    else:
        save_results(new_results)
        print("✅ Result deleted")


def view_all_results():
    results = load_results()

    if not results:
        print("No results found")
        return

    print("\n--- ALL RESULTS ---")
    for r in results:
        print(f"{r['roll']} | {r['name']} | {r['marks']}")


def view_student_result(username):
    results = load_results()

    for r in results:
        if r.get("username") == username:
            print("\n--- YOUR RESULT ---")
            print(f"Roll: {r['roll']}")
            print(f"Name: {r['name']}")
            print(f"Marks: {r['marks']}")
            return

    print("❌ No result found for you")
