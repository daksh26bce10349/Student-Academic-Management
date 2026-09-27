from student_manager import find_student
from marks_manager import subjects
from performance_analyzer import calculate_percentage
from performance_analyzer import calculate_grade

def student_report(students):
    print("\n=========================")
    print("      STUDENT REPORT")
    print("=========================")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student is None:
        print("Student not found")
        return

    print("\nRoll no: ",student["roll_no"])
    print("Name   :",student["name"])
    print("Class  :",student["class"])
    print("Section:",student["section"])
    print("\nMarks:")

    if len(student["marks"]) == 0:
        print("Marks not entered")
        return

    for subject in subjects:
        print(subject,":",student["marks"][subject])

    percentage = calculate_percentage(student)
    print("\nPercentage:",round(percentage,2),"%")
    print("Grade:",calculate_grade(percentage))

def class_report(students):
    print("\n=========================")
    print("       CLASS REPORT")
    print("=========================")

    for student in students:
        percentage = calculate_percentage(student)

        if percentage is not None:
            print(
                student["roll_no"],
                "-",
                student["name"],
                "-",
                round(percentage,2),
                "%",
                "-",
                calculate_grade(percentage)
            )
        else:
            print(
                student["roll_no"],
                "-",
                student["name"],
                "- Marks incomplete"
            )
            
