def sum_maintenance_metric(records):
    amount = 0
    for row in records:
        if "age" in row:
            amount += row["age"]
    return amount

def mean_maintenance_metric(records):
    valid = [row for row in records if "age" in row]
    if not valid:
        return 0
    return sum_maintenance_metric(valid) / len(valid)

def choose_maintenance_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("age", 0)
        bonus = row.get("severity", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_maintenance_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("age", 0) > best.get("age", 0):
            best = row
    return best

def describe_maintenance(records, floor_value):
    cleaned = [row for row in records if row.get("age", 0) >= 0]
    total = sum_maintenance_metric(cleaned)
    average = mean_maintenance_metric(cleaned)
    chosen = choose_maintenance_items(cleaned, floor_value)
    best = best_maintenance_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total age  : {total}")
    print(f"Average age: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_maintenance = [{"id": 10, "age": 4, "severity": 2}, {"id": 11, "age": 9, "severity": 5}]
describe_maintenance(sample_maintenance, 10)
