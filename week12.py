from services.registration_service import register
from utils.data_store import students, courses, registrations

def handle_register():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student not found")
        return

    cid = input("Enter Course ID: ")

    if cid not in courses:
        print("Invalid course")
        return

    if register(sid, cid):
        print("Registered successfully")
    else:
        print("Already registered")

def handle_view_registered():
    sid = input("Enter Student ID: ")

    if sid not in registrations:
        print("No courses")
        return

    print("Registered Courses:")
    for cid in registrations[sid]:
        print(cid)