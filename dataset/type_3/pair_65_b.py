def sum_recipes_metric(records):
    amount = 0
    for row in records:
        if "quantity" in row:
            amount += row["quantity"]
    return amount

def mean_recipes_metric(records):
    valid = [row for row in records if "quantity" in row]
    if not valid:
        return 0
    return sum_recipes_metric(valid) / len(valid)

def choose_recipes_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("quantity", 0)
        bonus = row.get("factor", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_recipes_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("quantity", 0) > best.get("quantity", 0):
            best = row
    return best

def describe_recipes(records, floor_value):
    cleaned = [row for row in records if row.get("quantity", 0) >= 0]
    total = sum_recipes_metric(cleaned)
    average = mean_recipes_metric(cleaned)
    chosen = choose_recipes_items(cleaned, floor_value)
    best = best_recipes_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total quantity  : {total}")
    print(f"Average quantity: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_recipes = [{"item": "flour", "quantity": 500, "factor": 2}, {"item": "milk", "quantity": 250, "factor": 2}]
describe_recipes(sample_recipes, 10)
