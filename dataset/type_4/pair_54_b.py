def total_inventory(products):
    return sum(map(lambda entry: entry["stock"], products))

def average_inventory(products):
    values = tuple(entry["stock"] for entry in products)
    return sum(values) / len(values) if values else 0

def maximum_inventory(products):
    return max(products, key=lambda entry: entry["stock"], default=None)

def select_inventory(products, minimum):
    return list(filter(lambda entry: entry["stock"] >= minimum, products))

def inventory_report(products, minimum):
    summary = (
        total_inventory(products),
        average_inventory(products),
        maximum_inventory(products),
        select_inventory(products, minimum),
    )
    labels = ("Total stock", "Average stock", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_inventory = [{"sku": "A1", "stock": 8}, {"sku": "B2", "stock": 2}, {"sku": "C3", "stock": 11}]
inventory_report(data_inventory, 10)
