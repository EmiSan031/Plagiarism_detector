def sum_steps_metric(records):
    amount = 0
    for row in records:
        if "steps" in row:
            amount += row["steps"]
    return amount

def mean_steps_metric(records):
    valid = [row for row in records if "steps" in row]
    if not valid:
        return 0
    return sum_steps_metric(valid) / len(valid)

def choose_steps_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("steps", 0)
        bonus = row.get("goal", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_steps_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("steps", 0) > best.get("steps", 0):
            best = row
    return best

def describe_steps(records, floor_value):
    cleaned = [row for row in records if row.get("steps", 0) >= 0]
    total = sum_steps_metric(cleaned)
    average = mean_steps_metric(cleaned)
    chosen = choose_steps_items(cleaned, floor_value)
    best = best_steps_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total steps  : {total}")
    print(f"Average steps: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_steps = [{"day": "Mon", "steps": 9000, "goal": 8000}, {"day": "Tue", "steps": 6500, "goal": 8000}]
describe_steps(sample_steps, 10)
