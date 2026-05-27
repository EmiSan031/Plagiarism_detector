def total_attendance(sessions):
    return sum(map(lambda entry: entry["present"], sessions))

def average_attendance(sessions):
    values = tuple(entry["present"] for entry in sessions)
    return sum(values) / len(values) if values else 0

def maximum_attendance(sessions):
    return max(sessions, key=lambda entry: entry["present"], default=None)

def select_attendance(sessions, minimum):
    return list(filter(lambda entry: entry["present"] >= minimum, sessions))

def attendance_report(sessions, minimum):
    summary = (
        total_attendance(sessions),
        average_attendance(sessions),
        maximum_attendance(sessions),
        select_attendance(sessions, minimum),
    )
    labels = ("Total present", "Average present", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_attendance = [{"student": "Ana", "present": 17}, {"student": "Luis", "present": 14}, {"student": "Mia", "present": 9}]
attendance_report(data_attendance, 10)
