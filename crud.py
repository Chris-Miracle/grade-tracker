import json
import os
import utils
import matplotlib.pyplot as plt

######## Create New Student ########
def create_student():
    # Load existing data first
    if os.path.exists("data/student_data.json"):
        with open("data/student_data.json", "r") as file:
            try:
                student_data = json.load(file)
            except json.JSONDecodeError:
                student_data = {"students": []}
    else:
        student_data = {"students": []}

    # 1. Create new Student
    student_id = utils.create_student_id(student_data)
    student_name = input("Enter student name: ").strip()
    student_age = int(input("Enter student age: ").strip())

    # Update grades for subjects
    maths_grade = int(input("Enter maths grade: ").strip())
    science_grade = int(input("Enter science grade: ").strip())
    english_grade = int(input("Enter english grade: ").strip())
    history_grade = int(input("Enter history grade: ").strip())
    attendance_days_present = int(input("Enter days present: ").strip())
    attendance_days_absent = int(input("Enter days absent: ").strip())
    remarks = input("Enter remarks: ").strip()

    # Calculate GPA
    gpa = utils.calculate_gpa(maths_grade, science_grade, english_grade, history_grade)

    # Create student dictionary
    student_data['students'].append({
        "student_id": student_id,
        "student_name": student_name,
        "student_age": student_age,
        "grades": {
            "maths": maths_grade,
            "science": science_grade,
            "english": english_grade,
            "history": history_grade
        },
        "attendance": {
            "days_present": attendance_days_present,
            "days_absent": attendance_days_absent
        },
        "remarks": remarks,
        "gpa" : round(gpa, 2)
    })

    # Sort Students by GPA
    student_data['students'] = sorted(student_data['students'], key=lambda x: x['gpa'], reverse=True)

    # Convert to JSON and Save back to file
    with open("data/student_data.json", "w") as file:
        json.dump(student_data, file, indent=4)

    print(f"Student ID: {student_id}, Created Student: {student_name}, {student_age} years old")

########## Update Student ##########
def update_student():
    # 2. Update Student
    student_id = input("Enter student id: ").strip()

    # Try to find the student
    student_found = False

    student_data = utils.load_data_from_file()

    for student in student_data["students"]:
        if str(student["student_id"]) == student_id:
            student_found = True
            print(f"Student found: {student['student_name']} ({student['student_age']} yrs old)")

            option = input("What do you want to update? Personal Info(1), Grades(2), Attendance(3), Remarks(4), All(5): ").strip()

            if option in ["1", "5"]:
                student["student_name"] = input("Enter new student name: ").strip()
                student["student_age"] = int(input("Enter new student age: ").strip())

            if option in ["2", "5"]:
                student["grades"]["maths"] = int(input("Enter maths grade: ").strip())
                student["grades"]["science"] = int(input("Enter science grade: ").strip())
                student["grades"]["english"] = int(input("Enter english grade: ").strip())
                student["grades"]["history"] = int(input("Enter history grade: ").strip())
                student["gpa"] = round(utils.calculate_gpa(student["grades"]["maths"], student["grades"]["science"], student["grades"]["english"], student["grades"]["history"]), 2)

            if option in ["3", "5"]:
                student["attendance"]["days_present"] = int(input("Enter days present: ").strip())
                student["attendance"]["days_absent"] = int(input("Enter days absent: ").strip())

            if option in ["4", "5"]:
                student["remarks"] = input("Enter remarks: ").strip()
                
            # Sort Students by GPA
            student_data['students'] = sorted(student_data['students'], key=lambda x: x['gpa'], reverse=True)

            # Save the updated data back to the file
            with open("data/student_data.json", "w") as file:
                json.dump(student_data, file, indent=4)
                break

            print("\n Student updated successfully!")
            print(f"ID: {student['student_id']} | Name: {student['student_name']} | Age: {student['student_age']}")
            print(f"Grades: {student['grades']}")
            break
    if not student_found:
        print("Student not found.")

########## Calculate Average Grade ##########
def calculate_average_grade():
    # 3. Calculate Average Grade Per Subject
    student_data = utils.load_data_from_file()
    for student in student_data["students"]:
        grades = student["grades"]
        average_grade = sum(grades.values()) / len(grades)
        print(f"Student: {student['student_name']}, Average Grade: {average_grade:.2f}")

########## View Students ##########
def view_students():
    # View All Students
    student_data = utils.load_data_from_file()
    students = student_data["students"]

    if not students:
        print("No students in the system.")
        return
    
    for student in students:
        print(f"Student ID: {student['student_id']}, Student Name: {student['student_name']}, Student Age: {student['student_age']}")


######## Visualize Grade Distribution ##########
def visualize_grade_distribution():
    # 4. Visualize Grade Distribution using Matplotlib
    # Load student data
    student_data = utils.load_data_from_file()
    grades = []

    # Collect all grades from all students
    for student in student_data["students"]:
        grades.extend(student["grades"].values())

    if not grades:
        print("No grades available to visualize.")
        return

    # Plot histogram
    plt.hist(grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.title('Grade Distribution')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
