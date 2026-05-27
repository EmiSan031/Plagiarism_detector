def sum_tasks_metric(records):
    amount = 0
    for row in records:
        if "done" in row:
            amount += row["done"]
    return amount

def mean_tasks_metric(records):
    valid = [row for row in records if "done" in row]
    if not valid:
        return 0
    return sum_tasks_metric(valid) / len(valid)

def choose_tasks_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("done", 0)
        bonus = row.get("priority", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_tasks_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("done", 0) > best.get("done", 0):
            best = row
    return best

def describe_tasks(records, floor_value):
    cleaned = [row for row in records if row.get("done", 0) >= 0]
    total = sum_tasks_metric(cleaned)
    average = mean_tasks_metric(cleaned)
    chosen = choose_tasks_items(cleaned, floor_value)
    best = best_tasks_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total done  : {total}")
    print(f"Average done: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_tasks = [{"title": "draft", "done": True, "priority": 2}, {"title": "test", "done": False, "priority": 5}]
describe_tasks(sample_tasks, 10)
