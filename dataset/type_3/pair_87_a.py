def total_parking(tickets):
    total = 0
    for item in tickets:
        total += item["hours"]
    return total

def average_parking(tickets):
    if not tickets:
        return 0
    return total_parking(tickets) / len(tickets)

def high_parking(tickets, minimum):
    selected = []
    for item in tickets:
        if item["hours"] >= minimum:
            selected.append(item)
    return selected

def parking_report(tickets, minimum):
    total = total_parking(tickets)
    average = average_parking(tickets)
    selected = high_parking(tickets, minimum)
    print(f"Records         : {tickets}")
    print(f"Total hours  : {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_parking = [{"plate": "XAA", "hours": 3, "price": 15}, {"plate": "YBB", "hours": 5, "price": 12}]
parking_report(example_parking, 10)
