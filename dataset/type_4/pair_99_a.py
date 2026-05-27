def total_classroom(rooms):
    result = 0
    for item in rooms:
        result = result + item["desks"]
    return result

def average_classroom(rooms):
    count = 0
    total = 0
    for item in rooms:
        count += 1
        total += item["desks"]
    if count == 0:
        return 0
    return total / count

def maximum_classroom(rooms):
    if not rooms:
        return None
    best = rooms[0]
    for item in rooms[1:]:
        if item["desks"] > best["desks"]:
            best = item
    return best

def select_classroom(rooms, minimum):
    selected = []
    for item in rooms:
        if item["desks"] >= minimum:
            selected.append(item)
    return selected

def classroom_report(rooms, minimum):
    total = total_classroom(rooms)
    average = average_classroom(rooms)
    best = maximum_classroom(rooms)
    selected = select_classroom(rooms, minimum)
    print(f"Total desks: {total}")
    print(f"Average desks: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_classroom = [{"room": "101", "desks": 30}, {"room": "102", "desks": 24}, {"room": "103", "desks": 28}]
classroom_report(data_classroom, 10)
