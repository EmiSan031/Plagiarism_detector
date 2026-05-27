def sum_routes_metric(records):
    amount = 0
    for row in records:
        if "distance" in row:
            amount += row["distance"]
    return amount

def mean_routes_metric(records):
    valid = [row for row in records if "distance" in row]
    if not valid:
        return 0
    return sum_routes_metric(valid) / len(valid)

def choose_routes_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("distance", 0)
        bonus = row.get("time", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_routes_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("distance", 0) > best.get("distance", 0):
            best = row
    return best

def describe_routes(records, floor_value):
    cleaned = [row for row in records if row.get("distance", 0) >= 0]
    total = sum_routes_metric(cleaned)
    average = mean_routes_metric(cleaned)
    chosen = choose_routes_items(cleaned, floor_value)
    best = best_routes_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total distance  : {total}")
    print(f"Average distance: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_routes = [{"name": "north", "distance": 12, "time": 28}, {"name": "west", "distance": 7, "time": 20}]
describe_routes(sample_routes, 10)
