def sum_bakery_metric(records):
    amount = 0
    for row in records:
        if "loaves" in row:
            amount += row["loaves"]
    return amount

def mean_bakery_metric(records):
    valid = [row for row in records if "loaves" in row]
    if not valid:
        return 0
    return sum_bakery_metric(valid) / len(valid)

def choose_bakery_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("loaves", 0)
        bonus = row.get("defects", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_bakery_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("loaves", 0) > best.get("loaves", 0):
            best = row
    return best

def describe_bakery(records, floor_value):
    cleaned = [row for row in records if row.get("loaves", 0) >= 0]
    total = sum_bakery_metric(cleaned)
    average = mean_bakery_metric(cleaned)
    chosen = choose_bakery_items(cleaned, floor_value)
    best = best_bakery_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total loaves  : {total}")
    print(f"Average loaves: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_bakery = [{"batch": "morning", "loaves": 80, "defects": 3}, {"batch": "noon", "loaves": 65, "defects": 1}]
describe_bakery(sample_bakery, 10)
