def sum_seats_metric(records):
    amount = 0
    for row in records:
        if "occupied" in row:
            amount += row["occupied"]
    return amount

def mean_seats_metric(records):
    valid = [row for row in records if "occupied" in row]
    if not valid:
        return 0
    return sum_seats_metric(valid) / len(valid)

def choose_seats_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("occupied", 0)
        bonus = row.get("capacity", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_seats_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("occupied", 0) > best.get("occupied", 0):
            best = row
    return best

def describe_seats(records, floor_value):
    cleaned = [row for row in records if row.get("occupied", 0) >= 0]
    total = sum_seats_metric(cleaned)
    average = mean_seats_metric(cleaned)
    chosen = choose_seats_items(cleaned, floor_value)
    best = best_seats_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total occupied  : {total}")
    print(f"Average occupied: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_seats = [{"car": "A", "occupied": 38, "capacity": 50}, {"car": "B", "occupied": 45, "capacity": 45}]
describe_seats(sample_seats, 10)
