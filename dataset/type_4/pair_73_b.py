def total_hours(shifts):
    return sum(map(lambda entry: entry["hours"], shifts))

def average_hours(shifts):
    values = tuple(entry["hours"] for entry in shifts)
    return sum(values) / len(values) if values else 0

def maximum_hours(shifts):
    return max(shifts, key=lambda entry: entry["hours"], default=None)

def select_hours(shifts, minimum):
    return list(filter(lambda entry: entry["hours"] >= minimum, shifts))

def hours_report(shifts, minimum):
    summary = (
        total_hours(shifts),
        average_hours(shifts),
        maximum_hours(shifts),
        select_hours(shifts, minimum),
    )
    labels = ("Total hours", "Average hours", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_hours = [{"worker": "Sam", "hours": 38}, {"worker": "Tia", "hours": 41}, {"worker": "Uma", "hours": 29}]
hours_report(data_hours, 10)
