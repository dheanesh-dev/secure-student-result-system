from admin import admin_menu
from student import student_menu

def main():
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()
