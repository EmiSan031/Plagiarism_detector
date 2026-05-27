def total_hours(shifts):
    total = 0
    for item in shifts:
        total += item["hours"]
    return total

def average_hours(shifts):
    if not shifts:
        return 0
    return total_hours(shifts) / len(shifts)

def high_hours(shifts, minimum):
    selected = []
    for item in shifts:
        if item["hours"] >= minimum:
            selected.append(item)
    return selected

def hours_report(shifts, minimum):
    total = total_hours(shifts)
    average = average_hours(shifts)
    selected = high_hours(shifts, minimum)
    print(f"Records         : {shifts}")
    print(f"Total hours  : {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_hours = [{"worker": "Sam", "hours": 38, "rate": 12}, {"worker": "Tia", "hours": 41, "rate": 13}]
hours_report(example_hours, 10)
