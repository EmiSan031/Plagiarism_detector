def total_smoothies(orders):
    result = 0
    for item in orders:
        result = result + item["cups"]
    return result

def average_smoothies(orders):
    count = 0
    total = 0
    for item in orders:
        count += 1
        total += item["cups"]
    if count == 0:
        return 0
    return total / count

def maximum_smoothies(orders):
    if not orders:
        return None
    best = orders[0]
    for item in orders[1:]:
        if item["cups"] > best["cups"]:
            best = item
    return best

def select_smoothies(orders, minimum):
    selected = []
    for item in orders:
        if item["cups"] >= minimum:
            selected.append(item)
    return selected

def smoothie_report(orders, minimum):
    total = total_smoothies(orders)
    average = average_smoothies(orders)
    best = maximum_smoothies(orders)
    selected = select_smoothies(orders, minimum)
    print(f"Total cups: {total}")
    print(f"Average cups: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_smoothies = [{"flavor": "berry", "cups": 3}, {"flavor": "mango", "cups": 2}, {"flavor": "lime", "cups": 5}]
smoothie_report(data_smoothies, 10)
