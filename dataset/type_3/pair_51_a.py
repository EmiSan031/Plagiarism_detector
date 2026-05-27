def total_attendance(sessions):
    total = 0
    for item in sessions:
        total += item["present"]
    return total

def average_attendance(sessions):
    if not sessions:
        return 0
    return total_attendance(sessions) / len(sessions)

def high_attendance(sessions, minimum):
    selected = []
    for item in sessions:
        if item["present"] >= minimum:
            selected.append(item)
    return selected

def attendance_report(sessions, minimum):
    total = total_attendance(sessions)
    average = average_attendance(sessions)
    selected = high_attendance(sessions, minimum)
    print(f"Records         : {sessions}")
    print(f"Total present  : {total}")
    print(f"Average present: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_attendance = [{"student": "Ana", "present": 17, "total": 20}, {"student": "Luis", "present": 14, "total": 18}]
attendance_report(example_attendance, 10)
