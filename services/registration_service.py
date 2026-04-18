from utils.data_store import registrations

def register_course(sid, cid):
    if sid not in registrations:
        registrations[sid] = []

    if cid in registrations[sid]:
        return False

    registrations[sid].append(cid)
    return True