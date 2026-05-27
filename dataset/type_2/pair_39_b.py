def sum_deliveries_clone(data_39):
    accumulator = 0
    for element in data_39:
        accumulator += element["miles_value"]
    return accumulator

def mean_deliveries_clone(data_39):
    if not data_39:
        return 0
    return sum_deliveries_clone(data_39) / len(data_39)

def count_large_deliveries_clone(data_39, floor):
    matches = 0
    for element in data_39:
        if element["miles_value"] >= floor:
            matches += 1
    return matches

def show_deliveries_clone(data_39, floor):
    accumulator = sum_deliveries_clone(data_39)
    mean_value = mean_deliveries_clone(data_39)
    matches = count_large_deliveries_clone(data_39, floor)
    print(f"Sum miles_value: {accumulator}")
    print(f"Mean miles_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_deliveries_clone = [{"code": "D1", "miles_value": 14}, {"code": "D2", "miles_value": 8}, {"code": "D3", "miles_value": 19}]
show_deliveries_clone(items_deliveries_clone, 10)
