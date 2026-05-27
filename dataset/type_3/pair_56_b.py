def sum_shipments_metric(records):
    amount = 0
    for row in records:
        if "weight" in row:
            amount += row["weight"]
    return amount

def mean_shipments_metric(records):
    valid = [row for row in records if "weight" in row]
    if not valid:
        return 0
    return sum_shipments_metric(valid) / len(valid)

def choose_shipments_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("weight", 0)
        bonus = row.get("distance", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_shipments_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("weight", 0) > best.get("weight", 0):
            best = row
    return best

def describe_shipments(records, floor_value):
    cleaned = [row for row in records if row.get("weight", 0) >= 0]
    total = sum_shipments_metric(cleaned)
    average = mean_shipments_metric(cleaned)
    chosen = choose_shipments_items(cleaned, floor_value)
    best = best_shipments_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total weight  : {total}")
    print(f"Average weight: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_shipments = [{"code": "X1", "weight": 4, "distance": 120}, {"code": "X2", "weight": 7, "distance": 80}]
describe_shipments(sample_shipments, 10)
