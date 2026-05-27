def sum_irrigation_metric(records):
    amount = 0
    for row in records:
        if "liters" in row:
            amount += row["liters"]
    return amount

def mean_irrigation_metric(records):
    valid = [row for row in records if "liters" in row]
    if not valid:
        return 0
    return sum_irrigation_metric(valid) / len(valid)

def choose_irrigation_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("liters", 0)
        bonus = row.get("area", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_irrigation_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("liters", 0) > best.get("liters", 0):
            best = row
    return best

def describe_irrigation(records, floor_value):
    cleaned = [row for row in records if row.get("liters", 0) >= 0]
    total = sum_irrigation_metric(cleaned)
    average = mean_irrigation_metric(cleaned)
    chosen = choose_irrigation_items(cleaned, floor_value)
    best = best_irrigation_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total liters  : {total}")
    print(f"Average liters: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_irrigation = [{"plot": "east", "liters": 300, "area": 40}, {"plot": "west", "liters": 260, "area": 35}]
describe_irrigation(sample_irrigation, 10)
