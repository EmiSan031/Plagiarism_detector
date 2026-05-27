def sum_commissions_metric(records):
    amount = 0
    for row in records:
        if "revenue" in row:
            amount += row["revenue"]
    return amount

def mean_commissions_metric(records):
    valid = [row for row in records if "revenue" in row]
    if not valid:
        return 0
    return sum_commissions_metric(valid) / len(valid)

def choose_commissions_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("revenue", 0)
        bonus = row.get("rate", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_commissions_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("revenue", 0) > best.get("revenue", 0):
            best = row
    return best

def describe_commissions(records, floor_value):
    cleaned = [row for row in records if row.get("revenue", 0) >= 0]
    total = sum_commissions_metric(cleaned)
    average = mean_commissions_metric(cleaned)
    chosen = choose_commissions_items(cleaned, floor_value)
    best = best_commissions_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total revenue  : {total}")
    print(f"Average revenue: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_commissions = [{"seller": "Ari", "revenue": 1200, "rate": 0.08}, {"seller": "Ben", "revenue": 950, "rate": 0.07}]
describe_commissions(sample_commissions, 10)
