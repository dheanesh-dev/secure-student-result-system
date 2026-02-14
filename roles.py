from results import add_student, add_or_update_marks, view_students


def admin_menu(session):
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Add Student")
        print("2. Add / Update Marks")
        print("3. View Students")
        print("4. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_or_update_marks()
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("👋 Logged out")
            break
        else:
            print("❌ Invalid option")


def teacher_menu(session):
    while True:
        print("\n=== TEACHER MENU ===")
        print("1. Add / Update Marks")
        print("2. View Students")
        print("3. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            add_or_update_marks()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("👋 Logged out")
            break
        else:
            print("❌ Invalid option")


def student_menu(session):
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. View My Result")
        print("2. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            view_students()
        elif choice == "2":
            print("👋 Logged out")
            break
        else:
            print("❌ Invalid option")
