def total_logs(events):
    return sum(map(lambda entry: entry["severity"], events))

def average_logs(events):
    values = tuple(entry["severity"] for entry in events)
    return sum(values) / len(values) if values else 0

def maximum_logs(events):
    return max(events, key=lambda entry: entry["severity"], default=None)

def select_logs(events, minimum):
    return list(filter(lambda entry: entry["severity"] >= minimum, events))

def log_report(events, minimum):
    summary = (
        total_logs(events),
        average_logs(events),
        maximum_logs(events),
        select_logs(events, minimum),
    )
    labels = ("Total severity", "Average severity", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_logs = [{"event": "login", "severity": 2}, {"event": "sync", "severity": 4}, {"event": "pay", "severity": 3}]
log_report(data_logs, 10)
