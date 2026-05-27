def total_attendance(sessions):
    result = 0
    for item in sessions:
        result = result + item["present"]
    return result

def average_attendance(sessions):
    count = 0
    total = 0
    for item in sessions:
        count += 1
        total += item["present"]
    if count == 0:
        return 0
    return total / count

def maximum_attendance(sessions):
    if not sessions:
        return None
    best = sessions[0]
    for item in sessions[1:]:
        if item["present"] > best["present"]:
            best = item
    return best

def select_attendance(sessions, minimum):
    selected = []
    for item in sessions:
        if item["present"] >= minimum:
            selected.append(item)
    return selected

def attendance_report(sessions, minimum):
    total = total_attendance(sessions)
    average = average_attendance(sessions)
    best = maximum_attendance(sessions)
    selected = select_attendance(sessions, minimum)
    print(f"Total present: {total}")
    print(f"Average present: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_attendance = [{"student": "Ana", "present": 17}, {"student": "Luis", "present": 14}, {"student": "Mia", "present": 9}]
attendance_report(data_attendance, 10)
