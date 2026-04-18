from utils.data_store import courses


def get_courses():
    # Return all available courses
    return courses


def is_valid_course(cid):
    # Check if course exists
    return cid in courses