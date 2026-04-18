from services.course_service import get_courses
from utils.display import show_error


def handle_view_courses():
    courses = get_courses()

    if not courses:
        show_error("No courses available!")
        return

    print("\nAvailable Courses:")
    for cid, cname in courses.items():
        print(f"{cid} - {cname}")