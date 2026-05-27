def total_shipments(packages):
    result = 0
    for item in packages:
        result = result + item["weight"]
    return result

def average_shipments(packages):
    count = 0
    total = 0
    for item in packages:
        count += 1
        total += item["weight"]
    if count == 0:
        return 0
    return total / count

def maximum_shipments(packages):
    if not packages:
        return None
    best = packages[0]
    for item in packages[1:]:
        if item["weight"] > best["weight"]:
            best = item
    return best

def select_shipments(packages, minimum):
    selected = []
    for item in packages:
        if item["weight"] >= minimum:
            selected.append(item)
    return selected

def shipment_report(packages, minimum):
    total = total_shipments(packages)
    average = average_shipments(packages)
    best = maximum_shipments(packages)
    selected = select_shipments(packages, minimum)
    print(f"Total weight: {total}")
    print(f"Average weight: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_shipments = [{"code": "X1", "weight": 4}, {"code": "X2", "weight": 7}, {"code": "X3", "weight": 2}]
shipment_report(data_shipments, 10)
