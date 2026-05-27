def sum_portfolio_metric(records):
    amount = 0
    for row in records:
        if "shares" in row:
            amount += row["shares"]
    return amount

def mean_portfolio_metric(records):
    valid = [row for row in records if "shares" in row]
    if not valid:
        return 0
    return sum_portfolio_metric(valid) / len(valid)

def choose_portfolio_items(records, floor_value):
    chosen = []
    for row in records:
        value = row.get("shares", 0)
        bonus = row.get("price", 0)
        if isinstance(bonus, bool):
            bonus = 1 if bonus else 0
        if value + bonus >= floor_value:
            chosen.append(row)
    return chosen

def best_portfolio_item(records):
    if not records:
        return None
    best = records[0]
    for row in records[1:]:
        if row.get("shares", 0) > best.get("shares", 0):
            best = row
    return best

def describe_portfolio(records, floor_value):
    cleaned = [row for row in records if row.get("shares", 0) >= 0]
    total = sum_portfolio_metric(cleaned)
    average = mean_portfolio_metric(cleaned)
    chosen = choose_portfolio_items(cleaned, floor_value)
    best = best_portfolio_item(cleaned)
    print(f"Clean records   : {cleaned}")
    print(f"Total shares  : {total}")
    print(f"Average shares: {average:.2f}")
    print(f"Chosen rows     : {len(chosen)}")
    print(f"Best row        : {best}")
    return chosen

sample_portfolio = [{"ticker": "AAA", "shares": 8, "price": 14}, {"ticker": "BBB", "shares": 5, "price": 22}]
describe_portfolio(sample_portfolio, 10)
