def sum_inventory_metric(records):
    amount = 0
    for row in records:
        if "stock" in row:
            amount += row["stock"]
    return amount

def mean_inventory_metric(records):
    valid = [row for row in records if "stock" in row]
    if not valid:
        return 0
    return sum_inventory_metric(valid) / len(valid)

def choose_inventory_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("stock", 0)
        bonus = row.get("minimum", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_inventory_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("stock", 0) > best.get("stock", 0):
            best = row
    return best

def describe_inventory(records, floor_value):
    cleaned = [row for row in records if row.get("stock", 0) >= 0]
    total = sum_inventory_metric(cleaned)
    average = mean_inventory_metric(cleaned)
    chosen = choose_inventory_items(cleaned, floor_value)
    best = best_inventory_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total stock  : {total}")
    print(f"Average stock: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_inventory = [{"sku": "A1", "stock": 8, "minimum": 5}, {"sku": "B2", "stock": 2, "minimum": 6}]
describe_inventory(sample_inventory, 10)
