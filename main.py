import crud

# Create a command line interface
# Options:
options = {
    "1": "Create new student",
    "2": "Update student grades",
    "3": "Calculate average grade per student",
    "4": "Exit"
}

while True:
    print("-" * 50)
    crud.view_students()
    print("-" * 50)
    # Print options
    print("\nPlease choose an option:")
    for key, value in options.items():
        print(f"{key}. {value}")

    # Get user input
    on = input("Enter option: ").strip()

    if on == "4":
        print("Exiting program...")
        break
    elif on == "1":
        crud.create_student()
    elif on == "2":
        crud.update_student()
    elif on == "3":
        crud.calculate_average_grade()
    else:
        print("Invalid option. Please try again.")


