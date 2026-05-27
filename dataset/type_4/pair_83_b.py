def total_warehouse(bins):
    return sum(map(lambda entry: entry["units"], bins))

def average_warehouse(bins):
    values = tuple(entry["units"] for entry in bins)
    return sum(values) / len(values) if values else 0

def maximum_warehouse(bins):
    return max(bins, key=lambda entry: entry["units"], default=None)

def select_warehouse(bins, minimum):
    return list(filter(lambda entry: entry["units"] >= minimum, bins))

def warehouse_report(bins, minimum):
    summary = (
        total_warehouse(bins),
        average_warehouse(bins),
        maximum_warehouse(bins),
        select_warehouse(bins, minimum),
    )
    labels = ("Total units", "Average units", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_warehouse = [{"bin": "R1", "units": 45}, {"bin": "R2", "units": 70}, {"bin": "R3", "units": 52}]
warehouse_report(data_warehouse, 10)
