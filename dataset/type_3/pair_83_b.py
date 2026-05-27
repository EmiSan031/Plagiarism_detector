def sum_warehouse_metric(records):
    amount = 0
    for row in records:
        if "units" in row:
            amount += row["units"]
    return amount

def mean_warehouse_metric(records):
    valid = [row for row in records if "units" in row]
    if not valid:
        return 0
    return sum_warehouse_metric(valid) / len(valid)

def choose_warehouse_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("units", 0)
        bonus = row.get("capacity", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_warehouse_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("units", 0) > best.get("units", 0):
            best = row
    return best

def describe_warehouse(records, floor_value):
    cleaned = [row for row in records if row.get("units", 0) >= 0]
    total = sum_warehouse_metric(cleaned)
    average = mean_warehouse_metric(cleaned)
    chosen = choose_warehouse_items(cleaned, floor_value)
    best = best_warehouse_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total units  : {total}")
    print(f"Average units: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_warehouse = [{"bin": "R1", "units": 45, "capacity": 60}, {"bin": "R2", "units": 70, "capacity": 65}]
describe_warehouse(sample_warehouse, 10)
