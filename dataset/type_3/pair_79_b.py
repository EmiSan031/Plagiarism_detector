def sum_classes_metric(records):
    amount = 0
    for row in records:
        if "students" in row:
            amount += row["students"]
    return amount

def mean_classes_metric(records):
    valid = [row for row in records if "students" in row]
    if not valid:
        return 0
    return sum_classes_metric(valid) / len(valid)

def choose_classes_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("students", 0)
        bonus = row.get("capacity", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_classes_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("students", 0) > best.get("students", 0):
            best = row
    return best

def describe_classes(records, floor_value):
    cleaned = [row for row in records if row.get("students", 0) >= 0]
    total = sum_classes_metric(cleaned)
    average = mean_classes_metric(cleaned)
    chosen = choose_classes_items(cleaned, floor_value)
    best = best_classes_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total students  : {total}")
    print(f"Average students: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_classes = [{"room": "A", "students": 28, "capacity": 30}, {"room": "B", "students": 33, "capacity": 32}]
describe_classes(sample_classes, 10)
