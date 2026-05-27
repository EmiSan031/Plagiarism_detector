def sum_smoothies_metric(records):
    amount = 0
    for row in records:
        if "cups" in row:
            amount += row["cups"]
    return amount

def mean_smoothies_metric(records):
    valid = [row for row in records if "cups" in row]
    if not valid:
        return 0
    return sum_smoothies_metric(valid) / len(valid)

def choose_smoothies_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("cups", 0)
        bonus = row.get("fruit_units", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_smoothies_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("cups", 0) > best.get("cups", 0):
            best = row
    return best

def describe_smoothies(records, floor_value):
    cleaned = [row for row in records if row.get("cups", 0) >= 0]
    total = sum_smoothies_metric(cleaned)
    average = mean_smoothies_metric(cleaned)
    chosen = choose_smoothies_items(cleaned, floor_value)
    best = best_smoothies_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total cups  : {total}")
    print(f"Average cups: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_smoothies = [{"flavor": "berry", "cups": 3, "fruit_units": 6}, {"flavor": "mango", "cups": 2, "fruit_units": 5}]
describe_smoothies(sample_smoothies, 10)
