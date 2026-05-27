def total_maintenance(tickets):
    total = 0
    for item in tickets:
        total += item["age"]
    return total

def average_maintenance(tickets):
    if not tickets:
        return 0
    return total_maintenance(tickets) / len(tickets)

def high_maintenance(tickets, minimum):
    selected = []
    for item in tickets:
        if item["age"] >= minimum:
            selected.append(item)
    return selected

def maintenance_report(tickets, minimum):
    total = total_maintenance(tickets)
    average = average_maintenance(tickets)
    selected = high_maintenance(tickets, minimum)
    print(f"Records         : {tickets}")
    print(f"Total age  : {total}")
    print(f"Average age: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_maintenance = [{"id": 10, "age": 4, "severity": 2}, {"id": 11, "age": 9, "severity": 5}]
maintenance_report(example_maintenance, 10)
