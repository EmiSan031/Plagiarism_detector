def total_hours(shifts):
    result = 0
    for item in shifts:
        result = result + item["hours"]
    return result

def average_hours(shifts):
    count = 0
    total = 0
    for item in shifts:
        count += 1
        total += item["hours"]
    if count == 0:
        return 0
    return total / count

def maximum_hours(shifts):
    if not shifts:
        return None
    best = shifts[0]
    for item in shifts[1:]:
        if item["hours"] > best["hours"]:
            best = item
    return best

def select_hours(shifts, minimum):
    selected = []
    for item in shifts:
        if item["hours"] >= minimum:
            selected.append(item)
    return selected

def hours_report(shifts, minimum):
    total = total_hours(shifts)
    average = average_hours(shifts)
    best = maximum_hours(shifts)
    selected = select_hours(shifts, minimum)
    print(f"Total hours: {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_hours = [{"worker": "Sam", "hours": 38}, {"worker": "Tia", "hours": 41}, {"worker": "Uma", "hours": 29}]
hours_report(data_hours, 10)
