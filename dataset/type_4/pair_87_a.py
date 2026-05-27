def total_parking(tickets):
    result = 0
    for item in tickets:
        result = result + item["hours"]
    return result

def average_parking(tickets):
    count = 0
    total = 0
    for item in tickets:
        count += 1
        total += item["hours"]
    if count == 0:
        return 0
    return total / count

def maximum_parking(tickets):
    if not tickets:
        return None
    best = tickets[0]
    for item in tickets[1:]:
        if item["hours"] > best["hours"]:
            best = item
    return best

def select_parking(tickets, minimum):
    selected = []
    for item in tickets:
        if item["hours"] >= minimum:
            selected.append(item)
    return selected

def parking_report(tickets, minimum):
    total = total_parking(tickets)
    average = average_parking(tickets)
    best = maximum_parking(tickets)
    selected = select_parking(tickets, minimum)
    print(f"Total hours: {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_parking = [{"plate": "XAA", "hours": 3}, {"plate": "YBB", "hours": 5}, {"plate": "ZCC", "hours": 1}]
parking_report(data_parking, 10)
