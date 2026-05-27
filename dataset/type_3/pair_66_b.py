def sum_hotel_metric(records):
    amount = 0
    for row in records:
        if "nights" in row:
            amount += row["nights"]
    return amount

def mean_hotel_metric(records):
    valid = [row for row in records if "nights" in row]
    if not valid:
        return 0
    return sum_hotel_metric(valid) / len(valid)

def choose_hotel_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("nights", 0)
        bonus = row.get("rate", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_hotel_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("nights", 0) > best.get("nights", 0):
            best = row
    return best

def describe_hotel(records, floor_value):
    cleaned = [row for row in records if row.get("nights", 0) >= 0]
    total = sum_hotel_metric(cleaned)
    average = mean_hotel_metric(cleaned)
    chosen = choose_hotel_items(cleaned, floor_value)
    best = best_hotel_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total nights  : {total}")
    print(f"Average nights: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_hotel = [{"guest": "Iris", "nights": 3, "rate": 90}, {"guest": "Leo", "nights": 2, "rate": 110}]
describe_hotel(sample_hotel, 10)
