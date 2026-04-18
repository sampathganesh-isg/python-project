import matplotlib.pyplot as plt
from utils.data_store import registrations, courses


def plot_course_enrollment():
    course_count = {}

    # Count students per course
    for sid in registrations:
        for cid in registrations[sid]:
            course_count[cid] = course_count.get(cid, 0) + 1

    if not course_count:
        print("No data to display!")
        return

    # Bar Graph
    plt.figure()
    plt.bar(course_count.keys(), course_count.values())
    plt.title("Course Enrollment")
    plt.xlabel("Course ID")
    plt.ylabel("Number of Students")
    plt.show()


def plot_course_distribution():
    course_count = {}

    for sid in registrations:
        for cid in registrations[sid]:
            course_count[cid] = course_count.get(cid, 0) + 1

    if not course_count:
        print("No data to display!")
        return

    # Pie Chart
    plt.figure()
    plt.pie(course_count.values(), labels=course_count.keys(), autopct='%1.1f%%')
    plt.title("Course Distribution")
    plt.show()