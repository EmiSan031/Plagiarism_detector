def total_maintenance(tickets):
    result = 0
    for item in tickets:
        result = result + item["severity"]
    return result

def average_maintenance(tickets):
    count = 0
    total = 0
    for item in tickets:
        count += 1
        total += item["severity"]
    if count == 0:
        return 0
    return total / count

def maximum_maintenance(tickets):
    if not tickets:
        return None
    best = tickets[0]
    for item in tickets[1:]:
        if item["severity"] > best["severity"]:
            best = item
    return best

def select_maintenance(tickets, minimum):
    selected = []
    for item in tickets:
        if item["severity"] >= minimum:
            selected.append(item)
    return selected

def maintenance_report(tickets, minimum):
    total = total_maintenance(tickets)
    average = average_maintenance(tickets)
    best = maximum_maintenance(tickets)
    selected = select_maintenance(tickets, minimum)
    print(f"Total severity: {total}")
    print(f"Average severity: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_maintenance = [{"id": 10, "severity": 2}, {"id": 11, "severity": 5}, {"id": 12, "severity": 4}]
maintenance_report(data_maintenance, 10)
