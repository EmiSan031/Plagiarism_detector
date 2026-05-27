def total_maintenance(tickets):
    return sum(map(lambda entry: entry["severity"], tickets))

def average_maintenance(tickets):
    values = tuple(entry["severity"] for entry in tickets)
    return sum(values) / len(values) if values else 0

def maximum_maintenance(tickets):
    return max(tickets, key=lambda entry: entry["severity"], default=None)

def select_maintenance(tickets, minimum):
    return list(filter(lambda entry: entry["severity"] >= minimum, tickets))

def maintenance_report(tickets, minimum):
    summary = (
        total_maintenance(tickets),
        average_maintenance(tickets),
        maximum_maintenance(tickets),
        select_maintenance(tickets, minimum),
    )
    labels = ("Total severity", "Average severity", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_maintenance = [{"id": 10, "severity": 2}, {"id": 11, "severity": 5}, {"id": 12, "severity": 4}]
maintenance_report(data_maintenance, 10)
