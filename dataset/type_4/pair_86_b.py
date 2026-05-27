def total_commissions(sales):
    return sum(map(lambda entry: entry["revenue"], sales))

def average_commissions(sales):
    values = tuple(entry["revenue"] for entry in sales)
    return sum(values) / len(values) if values else 0

def maximum_commissions(sales):
    return max(sales, key=lambda entry: entry["revenue"], default=None)

def select_commissions(sales, minimum):
    return list(filter(lambda entry: entry["revenue"] >= minimum, sales))

def commission_report(sales, minimum):
    summary = (
        total_commissions(sales),
        average_commissions(sales),
        maximum_commissions(sales),
        select_commissions(sales, minimum),
    )
    labels = ("Total revenue", "Average revenue", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_commissions = [{"seller": "Ari", "revenue": 1200}, {"seller": "Ben", "revenue": 950}, {"seller": "Cid", "revenue": 1410}]
commission_report(data_commissions, 10)
