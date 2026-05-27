def sum_parking_metric(records):
    amount = 0
    for row in records:
        if "hours" in row:
            amount += row["hours"]
    return amount

def mean_parking_metric(records):
    valid = [row for row in records if "hours" in row]
    if not valid:
        return 0
    return sum_parking_metric(valid) / len(valid)

def choose_parking_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("hours", 0)
        bonus = row.get("price", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_parking_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("hours", 0) > best.get("hours", 0):
            best = row
    return best

def describe_parking(records, floor_value):
    cleaned = [row for row in records if row.get("hours", 0) >= 0]
    total = sum_parking_metric(cleaned)
    average = mean_parking_metric(cleaned)
    chosen = choose_parking_items(cleaned, floor_value)
    best = best_parking_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total hours  : {total}")
    print(f"Average hours: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_parking = [{"plate": "XAA", "hours": 3, "price": 15}, {"plate": "YBB", "hours": 5, "price": 12}]
describe_parking(sample_parking, 10)
