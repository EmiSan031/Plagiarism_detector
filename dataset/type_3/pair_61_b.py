def sum_books_metric(records):
    amount = 0
    for row in records:
        if "pages" in row:
            amount += row["pages"]
    return amount

def mean_books_metric(records):
    valid = [row for row in records if "pages" in row]
    if not valid:
        return 0
    return sum_books_metric(valid) / len(valid)

def choose_books_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("pages", 0)
        bonus = row.get("chapters", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_books_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("pages", 0) > best.get("pages", 0):
            best = row
    return best

def describe_books(records, floor_value):
    cleaned = [row for row in records if row.get("pages", 0) >= 0]
    total = sum_books_metric(cleaned)
    average = mean_books_metric(cleaned)
    chosen = choose_books_items(cleaned, floor_value)
    best = best_books_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total pages  : {total}")
    print(f"Average pages: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_books = [{"title": "Blue", "pages": 210, "chapters": 12}, {"title": "Green", "pages": 145, "chapters": 9}]
describe_books(sample_books, 10)
