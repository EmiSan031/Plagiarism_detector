def total_utilities(bills):
    return sum(map(lambda entry: entry["usage"], bills))

def average_utilities(bills):
    values = tuple(entry["usage"] for entry in bills)
    return sum(values) / len(values) if values else 0

def maximum_utilities(bills):
    return max(bills, key=lambda entry: entry["usage"], default=None)

def select_utilities(bills, minimum):
    return list(filter(lambda entry: entry["usage"] >= minimum, bills))

def utility_report(bills, minimum):
    summary = (
        total_utilities(bills),
        average_utilities(bills),
        maximum_utilities(bills),
        select_utilities(bills, minimum),
    )
    labels = ("Total usage", "Average usage", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_utilities = [{"service": "water", "usage": 22}, {"service": "power", "usage": 180}, {"service": "gas", "usage": 34}]
utility_report(data_utilities, 10)
