def sum_soccer_metric(records):
    amount = 0
    for row in records:
        if "goals" in row:
            amount += row["goals"]
    return amount

def mean_soccer_metric(records):
    valid = [row for row in records if "goals" in row]
    if not valid:
        return 0
    return sum_soccer_metric(valid) / len(valid)

def choose_soccer_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("goals", 0)
        bonus = row.get("points", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_soccer_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("goals", 0) > best.get("goals", 0):
            best = row
    return best

def describe_soccer(records, floor_value):
    cleaned = [row for row in records if row.get("goals", 0) >= 0]
    total = sum_soccer_metric(cleaned)
    average = mean_soccer_metric(cleaned)
    chosen = choose_soccer_items(cleaned, floor_value)
    best = best_soccer_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total goals  : {total}")
    print(f"Average goals: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_soccer = [{"team": "Lions", "goals": 9, "points": 12}, {"team": "Waves", "goals": 7, "points": 10}]
describe_soccer(sample_soccer, 10)
