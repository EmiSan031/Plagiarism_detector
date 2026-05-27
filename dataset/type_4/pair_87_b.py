def total_parking(tickets):
    return sum(map(lambda entry: entry["hours"], tickets))

def average_parking(tickets):
    values = tuple(entry["hours"] for entry in tickets)
    return sum(values) / len(values) if values else 0

def maximum_parking(tickets):
    return max(tickets, key=lambda entry: entry["hours"], default=None)

def select_parking(tickets, minimum):
    return list(filter(lambda entry: entry["hours"] >= minimum, tickets))

def parking_report(tickets, minimum):
    summary = (
        total_parking(tickets),
        average_parking(tickets),
        maximum_parking(tickets),
        select_parking(tickets, minimum),
    )
    labels = ("Total hours", "Average hours", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_parking = [{"plate": "XAA", "hours": 3}, {"plate": "YBB", "hours": 5}, {"plate": "ZCC", "hours": 1}]
parking_report(data_parking, 10)
