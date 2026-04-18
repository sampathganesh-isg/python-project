from utils.display import show_menu
from controllers.student_controller import handle_add_student
from controllers.course_controller import handle_view_courses
from controllers.registration_controller import handle_register, handle_view_registered
from utils.charts import plot_course_enrollment, plot_course_distribution
def main():
    while True:
        show_menu()
        ch = input("Enter choice: ")

        if ch == "1":
            handle_add_student()
        elif ch == "2":
            handle_view_courses()
        elif ch == "3":
            handle_register()
        elif ch == "4":
            handle_view_registered()
        elif ch == "5":
            plot_course_enrollment()
            plot_course_distribution()

        elif ch == "6":
            break

if __name__ == "__main__":
    main()