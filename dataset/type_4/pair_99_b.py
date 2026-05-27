def total_classroom(rooms):
    return sum(map(lambda entry: entry["desks"], rooms))

def average_classroom(rooms):
    values = tuple(entry["desks"] for entry in rooms)
    return sum(values) / len(values) if values else 0

def maximum_classroom(rooms):
    return max(rooms, key=lambda entry: entry["desks"], default=None)

def select_classroom(rooms, minimum):
    return list(filter(lambda entry: entry["desks"] >= minimum, rooms))

def classroom_report(rooms, minimum):
    summary = (
        total_classroom(rooms),
        average_classroom(rooms),
        maximum_classroom(rooms),
        select_classroom(rooms, minimum),
    )
    labels = ("Total desks", "Average desks", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_classroom = [{"room": "101", "desks": 30}, {"room": "102", "desks": 24}, {"room": "103", "desks": 28}]
classroom_report(data_classroom, 10)
