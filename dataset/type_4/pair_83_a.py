def total_warehouse(bins):
    result = 0
    for item in bins:
        result = result + item["units"]
    return result

def average_warehouse(bins):
    count = 0
    total = 0
    for item in bins:
        count += 1
        total += item["units"]
    if count == 0:
        return 0
    return total / count

def maximum_warehouse(bins):
    if not bins:
        return None
    best = bins[0]
    for item in bins[1:]:
        if item["units"] > best["units"]:
            best = item
    return best

def select_warehouse(bins, minimum):
    selected = []
    for item in bins:
        if item["units"] >= minimum:
            selected.append(item)
    return selected

def warehouse_report(bins, minimum):
    total = total_warehouse(bins)
    average = average_warehouse(bins)
    best = maximum_warehouse(bins)
    selected = select_warehouse(bins, minimum)
    print(f"Total units: {total}")
    print(f"Average units: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_warehouse = [{"bin": "R1", "units": 45}, {"bin": "R2", "units": 70}, {"bin": "R3", "units": 52}]
warehouse_report(data_warehouse, 10)
