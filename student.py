def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. View Result")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Showing student result (demo)")
        elif choice == "2":
            print("Exiting student menu...")
            break
        else:
            print("Invalid choice. Try again.")
