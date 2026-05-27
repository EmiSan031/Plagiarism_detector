def sum_rentals_metric(records):
    amount = 0
    for row in records:
        if "days" in row:
            amount += row["days"]
    return amount

def mean_rentals_metric(records):
    valid = [row for row in records if "days" in row]
    if not valid:
        return 0
    return sum_rentals_metric(valid) / len(valid)

def choose_rentals_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("days", 0)
        bonus = row.get("daily_rate", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_rentals_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("days", 0) > best.get("days", 0):
            best = row
    return best

def describe_rentals(records, floor_value):
    cleaned = [row for row in records if row.get("days", 0) >= 0]
    total = sum_rentals_metric(cleaned)
    average = mean_rentals_metric(cleaned)
    chosen = choose_rentals_items(cleaned, floor_value)
    best = best_rentals_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total days  : {total}")
    print(f"Average days: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_rentals = [{"car": "sedan", "days": 3, "daily_rate": 45}, {"car": "van", "days": 2, "daily_rate": 70}]
describe_rentals(sample_rentals, 10)
