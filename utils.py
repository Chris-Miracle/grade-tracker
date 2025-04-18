import json

######## Load Data From File ##########
def load_data_from_file():
    try:
        with open("data/student_data.json", "r") as file:
            try:
                student_data = json.load(file)
                return student_data
            except json.JSONDecodeError:
                student_data = {"students": []}
                return student_data
    except FileNotFoundError:
        return {"students": []}
    

######### Create Student ID ##########
def create_student_id(student_data):
    # Create a unique student ID
    if student_data["students"]:
        last_student_id = max(student["student_id"] for student in student_data["students"])
        return last_student_id + 1
    else:
        return 1
    

########## Calculate GPA ##########
def calculate_gpa(maths_grade, science_grade, english_grade, history_grade):
    total_grade = maths_grade + science_grade + english_grade + history_grade
    gpa = total_grade / 4
    return gpa