from services.student_service import add_student

def handle_add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Dept: ")
    sem = input("Enter Sem: ")

    if add_student(sid, name, dept, sem):
        print("Student added!")
    else:
        print("Student exists!")