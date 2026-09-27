def find_student(students,roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student

    return None

def add_student(students):
    print("\n--- ADD STUDENT ---")

    roll_no = input("Enter roll number: ")

    if find_student(students,roll_no):
        print("The student already exists.")
        return

    name = input("Enter student name: ")
    class_name = input("Enter your class: ")
    section = input("Enter your section: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "class": class_name,
        "section": section,
        "marks": {}
    }
    students.append(student)

    print("Student added successfully")

def view_students(students):
    print("\n--- ALL STUDENTS ---")

    if len(students)==0:
        print("No students found")
        return

    for student in students:
        print("--------------------")
        print("Roll no:",student["roll_no"])
        print("Name   :",student["name"])
        print("Class  :",student["class"])
        print("Section:",student["section"])

def search_student(students):
    print("\n--- SEARCH STUDENT ---")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student:
        print("Roll no:",student["roll_no"])
        print("Name   :",student["name"])
        print("Class  :",student["class"])
        print("Section:",student["section"])
    else:
        print("Student not found")

def update_student(students):
    print("\n--- UPDATE STUDENT ---")

    roll_no = input(" Enter your roll no: ")

    student=find_student(students,roll_no)

    if student:
        student["name"] = input("Enter new name: ")
        student["class"] = input("Enter new class")
        student["section"] = input("Enter new section")
        print("Student Updated Successfully")

    else:
        print("Student not found")

def delete_student(students):
    print("\n--- DELETE STUDENT ---")

    roll_no = input("Enter your roll no: ")

    student = find_student(students,roll_no)

    if student:
        students.remove(student)
        print("Student deleted successfully")
    else:
        print("Student not found")

def student_menu(students):

    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again")


