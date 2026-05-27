def total_shipments(packages):
    return sum(map(lambda entry: entry["weight"], packages))

def average_shipments(packages):
    values = tuple(entry["weight"] for entry in packages)
    return sum(values) / len(values) if values else 0

def maximum_shipments(packages):
    return max(packages, key=lambda entry: entry["weight"], default=None)

def select_shipments(packages, minimum):
    return list(filter(lambda entry: entry["weight"] >= minimum, packages))

def shipment_report(packages, minimum):
    summary = (
        total_shipments(packages),
        average_shipments(packages),
        maximum_shipments(packages),
        select_shipments(packages, minimum),
    )
    labels = ("Total weight", "Average weight", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_shipments = [{"code": "X1", "weight": 4}, {"code": "X2", "weight": 7}, {"code": "X3", "weight": 2}]
shipment_report(data_shipments, 10)
