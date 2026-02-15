from auth import login_user, register_user
from admin import admin_menu
from teacher import teacher_menu
from student import student_menu


def main():
    while True:
        print("\n=== STUDENT RESULT MANAGEMENT SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            user = login_user()

            if user:
                # 🔑 ROLE-BASED ROUTING (THIS WAS MISSING)
                if user["role"] == "admin":
                    admin_menu(user)

                elif user["role"] == "teacher":
                    teacher_menu(user)

                elif user["role"] == "student":
                    student_menu(user)

                else:
                    print("Unknown role")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
