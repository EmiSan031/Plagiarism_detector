def sum_ratings_metric(records):
    amount = 0
    for row in records:
        if "stars" in row:
            amount += row["stars"]
    return amount

def mean_ratings_metric(records):
    valid = [row for row in records if "stars" in row]
    if not valid:
        return 0
    return sum_ratings_metric(valid) / len(valid)

def choose_ratings_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("stars", 0)
        bonus = row.get("votes", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_ratings_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("stars", 0) > best.get("stars", 0):
            best = row
    return best

def describe_ratings(records, floor_value):
    cleaned = [row for row in records if row.get("stars", 0) >= 0]
    total = sum_ratings_metric(cleaned)
    average = mean_ratings_metric(cleaned)
    chosen = choose_ratings_items(cleaned, floor_value)
    best = best_ratings_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total stars  : {total}")
    print(f"Average stars: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_ratings = [{"product": "pen", "stars": 4, "votes": 12}, {"product": "bag", "stars": 5, "votes": 7}]
describe_ratings(sample_ratings, 10)
