# ERP Student Course Registration System

students = {}
registrations = {}

# Predefined Courses
courses = {
    "C101": "Python Programming",
    "C102": "Data Structures",
    "C103": "Fundamentals of IOT",
    "C104": "Computer Programming",
    "C105": "Mathematics",
    "C106": "Lingua Skills",
}

# -------------------- ADD STUDENT --------------------
def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!\n")
        return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    semester = input("Enter Semester: ")

    students[student_id] = {
        "name": name,
        "department": department,
        "semester": semester
    }

    print("Student added successfully!\n")


# -------------------- VIEW COURSES --------------------
def view_courses():
    print("\nAvailable Courses:")
    for cid, cname in courses.items():
        print(f"{cid} - {cname}")
    print()


# -------------------- REGISTER COURSE --------------------
def register_course():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!\n")
        return

    view_courses()
    course_id = input("Enter Course ID to Register: ")

    if course_id not in courses:
        print("Invalid Course ID!\n")
        return

    if student_id not in registrations:
        registrations[student_id] = []

    if course_id in registrations[student_id]:
        print("Course already registered!\n")
        return

    registrations[student_id].append(course_id)
    print("Course registered successfully!\n")


# -------------------- VIEW REGISTERED COURSES --------------------
def view_registered_courses():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!\n")
        return

    if student_id not in registrations or not registrations[student_id]:
        print("No courses registered.\n")
        return

    print("\nRegistered Courses:")
    for cid in registrations[student_id]:
        print(f"{cid} - {courses[cid]}")
    print()


# -------------------- MAIN MENU --------------------
def main():
    while True:
        print("----- ERP Student Course Registration System -----")
        print("1. Add Student")
        print("2. View Available Courses")
        print("3. Register Course")
        print("4. View Registered Courses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            register_course()
        elif choice == "4":
            view_registered_courses()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.\n")


# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()