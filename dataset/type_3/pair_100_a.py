def total_smoothies(orders):
    total = 0
    for item in orders:
        total += item["cups"]
    return total

def average_smoothies(orders):
    if not orders:
        return 0
    return total_smoothies(orders) / len(orders)

def high_smoothies(orders, minimum):
    selected = []
    for item in orders:
        if item["cups"] >= minimum:
            selected.append(item)
    return selected

def smoothie_report(orders, minimum):
    total = total_smoothies(orders)
    average = average_smoothies(orders)
    selected = high_smoothies(orders, minimum)
    print(f"Records         : {orders}")
    print(f"Total cups  : {total}")
    print(f"Average cups: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_smoothies = [{"flavor": "berry", "cups": 3, "fruit_units": 6}, {"flavor": "mango", "cups": 2, "fruit_units": 5}]
smoothie_report(example_smoothies, 10)
