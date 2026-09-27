import json

def save_data(students):
    with open("data/students.json","w") as file:
        json.dump(students,file,indent=4)

def load_data():
    try:
        with open("data/students.json","r") as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        return []
    