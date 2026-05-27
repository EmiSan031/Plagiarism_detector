def total_portfolio(positions):
    result = 0
    for item in positions:
        result = result + item["shares"]
    return result

def average_portfolio(positions):
    count = 0
    total = 0
    for item in positions:
        count += 1
        total += item["shares"]
    if count == 0:
        return 0
    return total / count

def maximum_portfolio(positions):
    if not positions:
        return None
    best = positions[0]
    for item in positions[1:]:
        if item["shares"] > best["shares"]:
            best = item
    return best

def select_portfolio(positions, minimum):
    selected = []
    for item in positions:
        if item["shares"] >= minimum:
            selected.append(item)
    return selected

def portfolio_report(positions, minimum):
    total = total_portfolio(positions)
    average = average_portfolio(positions)
    best = maximum_portfolio(positions)
    selected = select_portfolio(positions, minimum)
    print(f"Total shares: {total}")
    print(f"Average shares: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_portfolio = [{"ticker": "AAA", "shares": 8}, {"ticker": "BBB", "shares": 5}, {"ticker": "CCC", "shares": 13}]
portfolio_report(data_portfolio, 10)
