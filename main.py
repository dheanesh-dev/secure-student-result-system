from auth import register_user, login_user
from admin import admin_menu
from student import student_menu
from teacher import teacher_menu



def main():
    while True:
        print("\n=== Secure Student Result Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            user = login_user()
            if user:
                role = user.get("role")

                if role == "admin":
                    admin_menu(user)
                elif role == "student":
                    student_menu(user)
                else:
                    print("❌ Unknown role. Contact admin.")

        elif choice == "3":
            print("👋 Exiting system. Bye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
