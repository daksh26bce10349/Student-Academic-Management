from student_manager import *
from marks_manager import *
from performance_analyzer import *
from report_generator import *
from data_manager import load_data, save_data

students = load_data()

while True:
    print("\n====================")
    print("STUDENT ACADEMIC MANAGEMENT SYSTEM")
    print("====================")
    print("1. Student Management")
    print("2. Marks Management")
    print("3. Performance Analysis")
    print("4. Student Report")
    print("5. Class Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_menu(students)

    elif choice == "2":
        marks_menu(students)

    elif choice == "3":
        performance_menu(students)

    elif choice == "4":
        student_report(students)

    elif choice == "5":
        class_report(students)

    elif choice == "6":
        save_data(students)
        print("Data saved successfully")
        print("Thank you for using the system")
        break

    else:
        print("Invalid choice. Please try again")

