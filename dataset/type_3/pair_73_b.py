def sum_hours_metric(records):
    amount = 0
    for row in records:
        if "hours" in row:
            amount += row["hours"]
    return amount

def mean_hours_metric(records):
    valid = [row for row in records if "hours" in row]
    if not valid:
        return 0
    return sum_hours_metric(valid) / len(valid)

def choose_hours_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("hours", 0)
        bonus = row.get("rate", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_hours_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("hours", 0) > best.get("hours", 0):
            best = row
    return best

def describe_hours(records, floor_value):
    cleaned = [row for row in records if row.get("hours", 0) >= 0]
    total = sum_hours_metric(cleaned)
    average = mean_hours_metric(cleaned)
    chosen = choose_hours_items(cleaned, floor_value)
    best = best_hours_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total hours  : {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_hours = [{"worker": "Sam", "hours": 38, "rate": 12}, {"worker": "Tia", "hours": 41, "rate": 13}]
describe_hours(sample_hours, 10)
