def total_portfolio(positions):
    return sum(map(lambda entry: entry["shares"], positions))

def average_portfolio(positions):
    values = tuple(entry["shares"] for entry in positions)
    return sum(values) / len(values) if values else 0

def maximum_portfolio(positions):
    return max(positions, key=lambda entry: entry["shares"], default=None)

def select_portfolio(positions, minimum):
    return list(filter(lambda entry: entry["shares"] >= minimum, positions))

def portfolio_report(positions, minimum):
    summary = (
        total_portfolio(positions),
        average_portfolio(positions),
        maximum_portfolio(positions),
        select_portfolio(positions, minimum),
    )
    labels = ("Total shares", "Average shares", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_portfolio = [{"ticker": "AAA", "shares": 8}, {"ticker": "BBB", "shares": 5}, {"ticker": "CCC", "shares": 13}]
portfolio_report(data_portfolio, 10)
