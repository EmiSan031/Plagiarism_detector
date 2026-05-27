def sum_energy_metric(records):
    amount = 0
    for row in records:
        if "kwh" in row:
            amount += row["kwh"]
    return amount

def mean_energy_metric(records):
    valid = [row for row in records if "kwh" in row]
    if not valid:
        return 0
    return sum_energy_metric(valid) / len(valid)

def choose_energy_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("kwh", 0)
        bonus = row.get("rate", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_energy_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("kwh", 0) > best.get("kwh", 0):
            best = row
    return best

def describe_energy(records, floor_value):
    cleaned = [row for row in records if row.get("kwh", 0) >= 0]
    total = sum_energy_metric(cleaned)
    average = mean_energy_metric(cleaned)
    chosen = choose_energy_items(cleaned, floor_value)
    best = best_energy_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total kwh  : {total}")
    print(f"Average kwh: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_energy = [{"meter": "M1", "kwh": 120, "rate": 1.5}, {"meter": "M2", "kwh": 95, "rate": 1.7}]
describe_energy(sample_energy, 10)
