from results import (
    add_result,
    update_result,
    delete_result,
    view_all_results
)


def admin_menu(user):
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add Result")
        print("2. Update Result")
        print("3. Delete Result")
        print("4. View All Results")
        print("5. Logout")

        choice = input("Select: ").strip()

        if choice == "1":
            add_result()

        elif choice == "2":
            update_result()

        elif choice == "3":
            delete_result()

        elif choice == "4":
            view_all_results()

        elif choice == "5":
            break

        else:
            print("Invalid choice")
