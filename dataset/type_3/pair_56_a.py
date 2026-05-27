def total_shipments(packages):
    total = 0
    for item in packages:
        total += item["weight"]
    return total

def average_shipments(packages):
    if not packages:
        return 0
    return total_shipments(packages) / len(packages)

def high_shipments(packages, minimum):
    selected = []
    for item in packages:
        if item["weight"] >= minimum:
            selected.append(item)
    return selected

def shipment_report(packages, minimum):
    total = total_shipments(packages)
    average = average_shipments(packages)
    selected = high_shipments(packages, minimum)
    print(f"Records         : {packages}")
    print(f"Total weight  : {total}")
    print(f"Average weight: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_shipments = [{"code": "X1", "weight": 4, "distance": 120}, {"code": "X2", "weight": 7, "distance": 80}]
shipment_report(example_shipments, 10)
