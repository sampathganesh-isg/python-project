from services.course_service import get_courses

def handle_view_courses():
    courses = get_courses()
    print("\nCourses:")
    for cid, cname in courses.items():
        print(cid, "-", cname)