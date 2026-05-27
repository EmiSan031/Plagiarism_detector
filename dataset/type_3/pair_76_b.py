def sum_movies_metric(records):
    amount = 0
    for row in records:
        if "minutes" in row:
            amount += row["minutes"]
    return amount

def mean_movies_metric(records):
    valid = [row for row in records if "minutes" in row]
    if not valid:
        return 0
    return sum_movies_metric(valid) / len(valid)

def choose_movies_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("minutes", 0)
        bonus = row.get("rating", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_movies_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("minutes", 0) > best.get("minutes", 0):
            best = row
    return best

def describe_movies(records, floor_value):
    cleaned = [row for row in records if row.get("minutes", 0) >= 0]
    total = sum_movies_metric(cleaned)
    average = mean_movies_metric(cleaned)
    chosen = choose_movies_items(cleaned, floor_value)
    best = best_movies_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total minutes  : {total}")
    print(f"Average minutes: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_movies = [{"title": "One", "minutes": 95, "rating": 8}, {"title": "Two", "minutes": 122, "rating": 7}]
describe_movies(sample_movies, 10)
