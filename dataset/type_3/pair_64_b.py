def sum_sensors_metric(records):
    amount = 0
    for row in records:
        if "value" in row:
            amount += row["value"]
    return amount

def mean_sensors_metric(records):
    valid = [row for row in records if "value" in row]
    if not valid:
        return 0
    return sum_sensors_metric(valid) / len(valid)

def choose_sensors_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("value", 0)
        bonus = row.get("threshold", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_sensors_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("value", 0) > best.get("value", 0):
            best = row
    return best

def describe_sensors(records, floor_value):
    cleaned = [row for row in records if row.get("value", 0) >= 0]
    total = sum_sensors_metric(cleaned)
    average = mean_sensors_metric(cleaned)
    chosen = choose_sensors_items(cleaned, floor_value)
    best = best_sensors_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total value  : {total}")
    print(f"Average value: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_sensors = [{"id": "s1", "value": 72, "threshold": 80}, {"id": "s2", "value": 91, "threshold": 85}]
describe_sensors(sample_sensors, 10)
