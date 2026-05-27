def sum_library_metric(records):
    amount = 0
    for row in records:
        if "days_late" in row:
            amount += row["days_late"]
    return amount

def mean_library_metric(records):
    valid = [row for row in records if "days_late" in row]
    if not valid:
        return 0
    return sum_library_metric(valid) / len(valid)

def choose_library_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("days_late", 0)
        bonus = row.get("daily_fee", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_library_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("days_late", 0) > best.get("days_late", 0):
            best = row
    return best

def describe_library(records, floor_value):
    cleaned = [row for row in records if row.get("days_late", 0) >= 0]
    total = sum_library_metric(cleaned)
    average = mean_library_metric(cleaned)
    chosen = choose_library_items(cleaned, floor_value)
    best = best_library_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total days_late  : {total}")
    print(f"Average days_late: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_library = [{"book": "A", "days_late": 2, "daily_fee": 3}, {"book": "B", "days_late": 0, "daily_fee": 3}]
describe_library(sample_library, 10)
