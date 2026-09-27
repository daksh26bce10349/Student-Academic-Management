from student_manager import find_student
from marks_manager import subjects

def calculate_percentage(student):

    if len(student["marks"]) != len(subjects):
        return None

    total=0
    for subject in subjects:
        total += student["marks"][subject]

    percentage = total / len(subjects)
    return percentage

def calculate_grade(percentage):

    if percentage >= 90:
        return "S"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage <= 40:
        return "E"

    else:
        return "F"

def student_performance(students):
    print("\n--- STUDENT PERFORMANCE ---")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student is None:
        print("Student not found")
        return

    percentage = calculate_percentage(student)

    if percentage is None:
        print("Please enter marks first.")
        return

    highest_subject = max(
        student["marks"],
        key=student["marks"].get
    )

    lowest_subject = min(
        student["marks"],
        key=student["marks"].get
    )

    print("\nName:",student["name"])
    print("Percentage:",round(percentage,2),"%")
    print("Greade:",calculate_grade(percentage))
    print("Strongest subject:",highest_subject)
    print("Weakest subject:",lowest_subject)

def class_performance(students):
    print("\n--- CLASS PERFORMANCE")

    total_percentage = 0
    count = 0
    highest_student = None
    lowest_student = None

    for student in students:
        percentage = calculate_percentage(student)

        if percentage is not None:
            total_percentage += percentage
            count += 1

            if highest_student is None:
                highest_student = student
                lowest_student = student

            else:
                if percentage > calculate_percentage(highest_student):
                    highest_student = student
                if percentage < calculate_percentage(lowest_student):
                    lowest_student = student

    if count == 0:
        print("No complete marks available")
        return

    average = total_percentage / count

    print("Students analyzed:",count)
    print("Class average:",round(average,2),"%")
    print(
        "Highest:",
        highest_student["name"],
        round(calculate_percentage(highest_student),2),
        "%"
    )
    print(
        "Lowest:",
        lowest_student["name"],
        round(calculate_percentage(lowest_student),2),
        "%"
    )

def performance_menu(students):

    while True:
        print("\n--- PERFORMANCE ANALYSIS ---")
        print("1. Student Performance")
        print("2. Class Performance")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_performance(students)

        elif choice == "2":
            class_performance(students)

        elif choice == "3":
            break

        else:
            print("Invalid Choice. Please try again")
