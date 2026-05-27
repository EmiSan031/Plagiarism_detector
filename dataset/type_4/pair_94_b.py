def total_seats(rows):
    return sum(map(lambda entry: entry["occupied"], rows))

def average_seats(rows):
    values = tuple(entry["occupied"] for entry in rows)
    return sum(values) / len(values) if values else 0

def maximum_seats(rows):
    return max(rows, key=lambda entry: entry["occupied"], default=None)

def select_seats(rows, minimum):
    return list(filter(lambda entry: entry["occupied"] >= minimum, rows))

def seat_report(rows, minimum):
    summary = (
        total_seats(rows),
        average_seats(rows),
        maximum_seats(rows),
        select_seats(rows, minimum),
    )
    labels = ("Total occupied", "Average occupied", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_seats = [{"car": "A", "occupied": 38}, {"car": "B", "occupied": 45}, {"car": "C", "occupied": 22}]
seat_report(data_seats, 10)
