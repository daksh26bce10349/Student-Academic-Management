from student_manager import find_student 

subjects = [
    "Physics",
    "Chemistry",
    "Mathematics",
    "Englsih",
    "Computer Science"
]

def enter_marks(students):
    print("\n--- ENTER MARKS ---")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student is None:
        print("Student not found")
        return

    print("Enter marks out of 100.")

    for subject in subjects:
        while True:
            try:
                marks = float(input(subject + ": "))

                if 0 <= marks <=100:
                    student["marks"][subject] = marks
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a number")

    print("Marks saved successfully")

def view_marks(students):
    print("\n--- VIEW MARKS ---")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student is None:
        print("Student not found")
        return

    if len(student["marks"]) == 0:
        print("Marks not entered")
        return

    print("Student: ",student["name"])

    for subject in subjects:
        print(subject,":",student["marks"][subject])

def marks_menu(students):

    while True:
        print("\n--- MARKS MANAGEMENT ---")
        print("1. Enter/Update Marks")
        print("2. View Marks")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            enter_marks(students)

        elif choice == "2":
            view_marks(students)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again")

