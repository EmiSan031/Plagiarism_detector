def total_logs(events):
    total = 0
    for item in events:
        total += item["severity"]
    return total

def average_logs(events):
    if not events:
        return 0
    return total_logs(events) / len(events)

def high_logs(events, minimum):
    selected = []
    for item in events:
        if item["severity"] >= minimum:
            selected.append(item)
    return selected

def log_report(events, minimum):
    total = total_logs(events)
    average = average_logs(events)
    selected = high_logs(events, minimum)
    print(f"Records         : {events}")
    print(f"Total severity  : {total}")
    print(f"Average severity: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_logs = [{"event": "login", "severity": 2, "duration": 5}, {"event": "sync", "severity": 4, "duration": 18}]
log_report(example_logs, 10)
