def sum_classroom_metric(records):
    amount = 0
    for row in records:
        if "desks" in row:
            amount += row["desks"]
    return amount

def mean_classroom_metric(records):
    valid = [row for row in records if "desks" in row]
    if not valid:
        return 0
    return sum_classroom_metric(valid) / len(valid)

def choose_classroom_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("desks", 0)
        bonus = row.get("students", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_classroom_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("desks", 0) > best.get("desks", 0):
            best = row
    return best

def describe_classroom(records, floor_value):
    cleaned = [row for row in records if row.get("desks", 0) >= 0]
    total = sum_classroom_metric(cleaned)
    average = mean_classroom_metric(cleaned)
    chosen = choose_classroom_items(cleaned, floor_value)
    best = best_classroom_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total desks  : {total}")
    print(f"Average desks: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_classroom = [{"room": "101", "desks": 30, "students": 27}, {"room": "102", "desks": 24, "students": 29}]
describe_classroom(sample_classroom, 10)
