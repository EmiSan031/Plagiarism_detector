def total_logs(events):
    result = 0
    for item in events:
        result = result + item["severity"]
    return result

def average_logs(events):
    count = 0
    total = 0
    for item in events:
        count += 1
        total += item["severity"]
    if count == 0:
        return 0
    return total / count

def maximum_logs(events):
    if not events:
        return None
    best = events[0]
    for item in events[1:]:
        if item["severity"] > best["severity"]:
            best = item
    return best

def select_logs(events, minimum):
    selected = []
    for item in events:
        if item["severity"] >= minimum:
            selected.append(item)
    return selected

def log_report(events, minimum):
    total = total_logs(events)
    average = average_logs(events)
    best = maximum_logs(events)
    selected = select_logs(events, minimum)
    print(f"Total severity: {total}")
    print(f"Average severity: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_logs = [{"event": "login", "severity": 2}, {"event": "sync", "severity": 4}, {"event": "pay", "severity": 3}]
log_report(data_logs, 10)
