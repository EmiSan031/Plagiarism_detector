def total_utilities(bills):
    total = 0
    for item in bills:
        total += item["usage"]
    return total

def average_utilities(bills):
    if not bills:
        return 0
    return total_utilities(bills) / len(bills)

def high_utilities(bills, minimum):
    selected = []
    for item in bills:
        if item["usage"] >= minimum:
            selected.append(item)
    return selected

def utility_report(bills, minimum):
    total = total_utilities(bills)
    average = average_utilities(bills)
    selected = high_utilities(bills, minimum)
    print(f"Records         : {bills}")
    print(f"Total usage  : {total}")
    print(f"Average usage: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_utilities = [{"service": "water", "usage": 22, "unit_price": 4}, {"service": "power", "usage": 180, "unit_price": 2}]
utility_report(example_utilities, 10)
