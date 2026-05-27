def total_commissions(sales):
    total = 0
    for item in sales:
        total += item["revenue"]
    return total

def average_commissions(sales):
    if not sales:
        return 0
    return total_commissions(sales) / len(sales)

def high_commissions(sales, minimum):
    selected = []
    for item in sales:
        if item["revenue"] >= minimum:
            selected.append(item)
    return selected

def commission_report(sales, minimum):
    total = total_commissions(sales)
    average = average_commissions(sales)
    selected = high_commissions(sales, minimum)
    print(f"Records         : {sales}")
    print(f"Total revenue  : {total}")
    print(f"Average revenue: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_commissions = [{"seller": "Ari", "revenue": 1200, "rate": 0.08}, {"seller": "Ben", "revenue": 950, "rate": 0.07}]
commission_report(example_commissions, 10)
