from utils.data_store import students

def add_student(sid, name, dept, sem):
    if sid in students:
        return False
    students[sid] = {"name": name, "dept": dept, "sem": sem}
    return True