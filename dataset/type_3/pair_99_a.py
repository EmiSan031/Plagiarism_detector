def total_classroom(rooms):
    total = 0
    for item in rooms:
        total += item["desks"]
    return total

def average_classroom(rooms):
    if not rooms:
        return 0
    return total_classroom(rooms) / len(rooms)

def high_classroom(rooms, minimum):
    selected = []
    for item in rooms:
        if item["desks"] >= minimum:
            selected.append(item)
    return selected

def classroom_report(rooms, minimum):
    total = total_classroom(rooms)
    average = average_classroom(rooms)
    selected = high_classroom(rooms, minimum)
    print(f"Records         : {rooms}")
    print(f"Total desks  : {total}")
    print(f"Average desks: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_classroom = [{"room": "101", "desks": 30, "students": 27}, {"room": "102", "desks": 24, "students": 29}]
classroom_report(example_classroom, 10)
