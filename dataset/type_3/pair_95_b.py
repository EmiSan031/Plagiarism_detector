def sum_aquarium_metric(records):
    amount = 0
    for row in records:
        if "ph" in row:
            amount += row["ph"]
    return amount

def mean_aquarium_metric(records):
    valid = [row for row in records if "ph" in row]
    if not valid:
        return 0
    return sum_aquarium_metric(valid) / len(valid)

def choose_aquarium_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("ph", 0)
        bonus = row.get("temperature", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_aquarium_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("ph", 0) > best.get("ph", 0):
            best = row
    return best

def describe_aquarium(records, floor_value):
    cleaned = [row for row in records if row.get("ph", 0) >= 0]
    total = sum_aquarium_metric(cleaned)
    average = mean_aquarium_metric(cleaned)
    chosen = choose_aquarium_items(cleaned, floor_value)
    best = best_aquarium_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total ph  : {total}")
    print(f"Average ph: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_aquarium = [{"tank": "one", "ph": 7.1, "temperature": 25}, {"tank": "two", "ph": 6.6, "temperature": 27}]
describe_aquarium(sample_aquarium, 10)
