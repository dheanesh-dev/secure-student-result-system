from results import add_result, update_result


def teacher_menu(user):
    while True:
        print("\n=== TEACHER MENU ===")
        print("1. Add Result")
        print("2. Update Result")
        print("3. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            add_result()

        elif choice == "2":
            update_result()

        elif choice == "3":
            break

        else:
            print("Invalid choice")
