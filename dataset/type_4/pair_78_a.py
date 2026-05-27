def total_utilities(bills):
    result = 0
    for item in bills:
        result = result + item["usage"]
    return result

def average_utilities(bills):
    count = 0
    total = 0
    for item in bills:
        count += 1
        total += item["usage"]
    if count == 0:
        return 0
    return total / count

def maximum_utilities(bills):
    if not bills:
        return None
    best = bills[0]
    for item in bills[1:]:
        if item["usage"] > best["usage"]:
            best = item
    return best

def select_utilities(bills, minimum):
    selected = []
    for item in bills:
        if item["usage"] >= minimum:
            selected.append(item)
    return selected

def utility_report(bills, minimum):
    total = total_utilities(bills)
    average = average_utilities(bills)
    best = maximum_utilities(bills)
    selected = select_utilities(bills, minimum)
    print(f"Total usage: {total}")
    print(f"Average usage: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_utilities = [{"service": "water", "usage": 22}, {"service": "power", "usage": 180}, {"service": "gas", "usage": 34}]
utility_report(data_utilities, 10)
