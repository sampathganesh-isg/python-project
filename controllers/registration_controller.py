from services.registration_service import register_course
from utils.data_store import students, courses, registrations
from utils.display import show_success, show_error


def handle_register():
    sid = input("Enter Student ID: ")

    # Check student
    if sid not in students:
        show_error("Student not found!")
        return

    cid = input("Enter Course ID: ")

    # Check course
    if cid not in courses:
        show_error("Invalid Course ID!")
        return

    # Register course
    result = register_course(sid, cid)

    if result:
        show_success("Course registered successfully!")
    else:
        show_error("Course already registered!")


def handle_view_registered():
    sid = input("Enter Student ID: ")

    if sid not in students:
        show_error("Student not found!")
        return

    if sid not in registrations or not registrations[sid]:
        show_error("No courses registered!")
        return

    print("\nRegistered Courses:")
    for cid in registrations[sid]:
        print(f"{cid} - {courses[cid]}")