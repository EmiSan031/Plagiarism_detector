def total_seats(rows):
    result = 0
    for item in rows:
        result = result + item["occupied"]
    return result

def average_seats(rows):
    count = 0
    total = 0
    for item in rows:
        count += 1
        total += item["occupied"]
    if count == 0:
        return 0
    return total / count

def maximum_seats(rows):
    if not rows:
        return None
    best = rows[0]
    for item in rows[1:]:
        if item["occupied"] > best["occupied"]:
            best = item
    return best

def select_seats(rows, minimum):
    selected = []
    for item in rows:
        if item["occupied"] >= minimum:
            selected.append(item)
    return selected

def seat_report(rows, minimum):
    total = total_seats(rows)
    average = average_seats(rows)
    best = maximum_seats(rows)
    selected = select_seats(rows, minimum)
    print(f"Total occupied: {total}")
    print(f"Average occupied: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_seats = [{"car": "A", "occupied": 38}, {"car": "B", "occupied": 45}, {"car": "C", "occupied": 22}]
seat_report(data_seats, 10)
