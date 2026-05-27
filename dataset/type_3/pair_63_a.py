def total_portfolio(positions):
    total = 0
    for item in positions:
        total += item["shares"]
    return total

def average_portfolio(positions):
    if not positions:
        return 0
    return total_portfolio(positions) / len(positions)

def high_portfolio(positions, minimum):
    selected = []
    for item in positions:
        if item["shares"] >= minimum:
            selected.append(item)
    return selected

def portfolio_report(positions, minimum):
    total = total_portfolio(positions)
    average = average_portfolio(positions)
    selected = high_portfolio(positions, minimum)
    print(f"Records         : {positions}")
    print(f"Total shares  : {total}")
    print(f"Average shares: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_portfolio = [{"ticker": "AAA", "shares": 8, "price": 14}, {"ticker": "BBB", "shares": 5, "price": 22}]
portfolio_report(example_portfolio, 10)
