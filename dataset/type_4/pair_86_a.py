def total_commissions(sales):
    result = 0
    for item in sales:
        result = result + item["revenue"]
    return result

def average_commissions(sales):
    count = 0
    total = 0
    for item in sales:
        count += 1
        total += item["revenue"]
    if count == 0:
        return 0
    return total / count

def maximum_commissions(sales):
    if not sales:
        return None
    best = sales[0]
    for item in sales[1:]:
        if item["revenue"] > best["revenue"]:
            best = item
    return best

def select_commissions(sales, minimum):
    selected = []
    for item in sales:
        if item["revenue"] >= minimum:
            selected.append(item)
    return selected

def commission_report(sales, minimum):
    total = total_commissions(sales)
    average = average_commissions(sales)
    best = maximum_commissions(sales)
    selected = select_commissions(sales, minimum)
    print(f"Total revenue: {total}")
    print(f"Average revenue: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_commissions = [{"seller": "Ari", "revenue": 1200}, {"seller": "Ben", "revenue": 950}, {"seller": "Cid", "revenue": 1410}]
commission_report(data_commissions, 10)
