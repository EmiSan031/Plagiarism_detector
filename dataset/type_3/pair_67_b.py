def sum_invoices_metric(records):
    amount = 0
    for row in records:
        if "price" in row:
            amount += row["price"]
    return amount

def mean_invoices_metric(records):
    valid = [row for row in records if "price" in row]
    if not valid:
        return 0
    return sum_invoices_metric(valid) / len(valid)

def choose_invoices_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("price", 0)
        bonus = row.get("tax", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_invoices_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("price", 0) > best.get("price", 0):
            best = row
    return best

def describe_invoices(records, floor_value):
    cleaned = [row for row in records if row.get("price", 0) >= 0]
    total = sum_invoices_metric(cleaned)
    average = mean_invoices_metric(cleaned)
    chosen = choose_invoices_items(cleaned, floor_value)
    best = best_invoices_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total price  : {total}")
    print(f"Average price: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_invoices = [{"item": "desk", "price": 180, "tax": 0.16}, {"item": "lamp", "price": 40, "tax": 0.16}]
describe_invoices(sample_invoices, 10)
