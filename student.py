from results import view_student_result


def student_menu(user):
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. View My Result")
        print("2. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            view_student_result(user["username"])

        elif choice == "2":
            break

        else:
            print("Invalid choice")
