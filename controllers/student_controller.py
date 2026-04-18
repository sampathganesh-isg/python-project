from services.student_service import add_student
from utils.display import show_success, show_error


def handle_add_student():
    sid = input("Enter Student ID: ")

    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")

    result = add_student(sid, name, dept, sem)

    if result:
        show_success("Student added successfully!")
    else:
        show_error("Student ID already exists!")