def sum_queue_metric(records):
    amount = 0
    for row in records:
        if "minutes" in row:
            amount += row["minutes"]
    return amount

def mean_queue_metric(records):
    valid = [row for row in records if "minutes" in row]
    if not valid:
        return 0
    return sum_queue_metric(valid) / len(valid)

def choose_queue_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("minutes", 0)
        bonus = row.get("priority", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_queue_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("minutes", 0) > best.get("minutes", 0):
            best = row
    return best

def describe_queue(records, floor_value):
    cleaned = [row for row in records if row.get("minutes", 0) >= 0]
    total = sum_queue_metric(cleaned)
    average = mean_queue_metric(cleaned)
    chosen = choose_queue_items(cleaned, floor_value)
    best = best_queue_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total minutes  : {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_queue = [{"job": "print", "minutes": 6, "priority": 2}, {"job": "scan", "minutes": 3, "priority": 1}]
describe_queue(sample_queue, 10)
