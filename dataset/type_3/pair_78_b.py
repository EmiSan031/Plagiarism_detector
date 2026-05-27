def sum_utilities_metric(records):
    amount = 0
    for row in records:
        if "usage" in row:
            amount += row["usage"]
    return amount

def mean_utilities_metric(records):
    valid = [row for row in records if "usage" in row]
    if not valid:
        return 0
    return sum_utilities_metric(valid) / len(valid)

def choose_utilities_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("usage", 0)
        bonus = row.get("unit_price", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_utilities_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("usage", 0) > best.get("usage", 0):
            best = row
    return best

def describe_utilities(records, floor_value):
    cleaned = [row for row in records if row.get("usage", 0) >= 0]
    total = sum_utilities_metric(cleaned)
    average = mean_utilities_metric(cleaned)
    chosen = choose_utilities_items(cleaned, floor_value)
    best = best_utilities_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total usage  : {total}")
    print(f"Average usage: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_utilities = [{"service": "water", "usage": 22, "unit_price": 4}, {"service": "power", "usage": 180, "unit_price": 2}]
describe_utilities(sample_utilities, 10)
