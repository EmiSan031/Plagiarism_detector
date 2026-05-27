def sum_meals_metric(records):
    amount = 0
    for row in records:
        if "calories" in row:
            amount += row["calories"]
    return amount

def mean_meals_metric(records):
    valid = [row for row in records if "calories" in row]
    if not valid:
        return 0
    return sum_meals_metric(valid) / len(valid)

def choose_meals_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("calories", 0)
        bonus = row.get("protein", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_meals_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("calories", 0) > best.get("calories", 0):
            best = row
    return best

def describe_meals(records, floor_value):
    cleaned = [row for row in records if row.get("calories", 0) >= 0]
    total = sum_meals_metric(cleaned)
    average = mean_meals_metric(cleaned)
    chosen = choose_meals_items(cleaned, floor_value)
    best = best_meals_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total calories  : {total}")
    print(f"Average calories: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_meals = [{"meal": "oats", "calories": 280, "protein": 11}, {"meal": "salad", "calories": 190, "protein": 7}]
describe_meals(sample_meals, 10)
