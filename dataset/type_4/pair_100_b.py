def total_smoothies(orders):
    return sum(map(lambda entry: entry["cups"], orders))

def average_smoothies(orders):
    values = tuple(entry["cups"] for entry in orders)
    return sum(values) / len(values) if values else 0

def maximum_smoothies(orders):
    return max(orders, key=lambda entry: entry["cups"], default=None)

def select_smoothies(orders, minimum):
    return list(filter(lambda entry: entry["cups"] >= minimum, orders))

def smoothie_report(orders, minimum):
    summary = (
        total_smoothies(orders),
        average_smoothies(orders),
        maximum_smoothies(orders),
        select_smoothies(orders, minimum),
    )
    labels = ("Total cups", "Average cups", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_smoothies = [{"flavor": "berry", "cups": 3}, {"flavor": "mango", "cups": 2}, {"flavor": "lime", "cups": 5}]
smoothie_report(data_smoothies, 10)
