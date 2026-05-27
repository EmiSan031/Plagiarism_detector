def total_warehouse(bins):
    total = 0
    for item in bins:
        total += item["units"]
    return total

def average_warehouse(bins):
    if not bins:
        return 0
    return total_warehouse(bins) / len(bins)

def high_warehouse(bins, minimum):
    selected = []
    for item in bins:
        if item["units"] >= minimum:
            selected.append(item)
    return selected

def warehouse_report(bins, minimum):
    total = total_warehouse(bins)
    average = average_warehouse(bins)
    selected = high_warehouse(bins, minimum)
    print(f"Records         : {bins}")
    print(f"Total units  : {total}")
    print(f"Average units: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_warehouse = [{"bin": "R1", "units": 45, "capacity": 60}, {"bin": "R2", "units": 70, "capacity": 65}]
warehouse_report(example_warehouse, 10)
