def total_seats(rows):
    total = 0
    for item in rows:
        total += item["occupied"]
    return total

def average_seats(rows):
    if not rows:
        return 0
    return total_seats(rows) / len(rows)

def high_seats(rows, minimum):
    selected = []
    for item in rows:
        if item["occupied"] >= minimum:
            selected.append(item)
    return selected

def seat_report(rows, minimum):
    total = total_seats(rows)
    average = average_seats(rows)
    selected = high_seats(rows, minimum)
    print(f"Records         : {rows}")
    print(f"Total occupied  : {total}")
    print(f"Average occupied: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_seats = [{"car": "A", "occupied": 38, "capacity": 50}, {"car": "B", "occupied": 45, "capacity": 45}]
seat_report(example_seats, 10)
