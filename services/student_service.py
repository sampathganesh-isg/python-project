from utils.data_store import students


def add_student(sid, name, dept, sem):
    # Check duplicate ID
    if sid in students:
        return False

    # Add student to data store
    students[sid] = {
        "name": name,
        "department": dept,
        "semester": sem
    }

    return True


def get_student(sid):
    return students.get(sid, None)


def get_all_students():
    return students