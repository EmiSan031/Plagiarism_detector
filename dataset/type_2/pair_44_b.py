def sum_plantsales_clone(data_44):
    accumulator = 0
    for element in data_44:
        accumulator += element["units_value"]
    return accumulator

def mean_plantsales_clone(data_44):
    if not data_44:
        return 0
    return sum_plantsales_clone(data_44) / len(data_44)

def count_large_plantsales_clone(data_44, floor):
    matches = 0
    for element in data_44:
        if element["units_value"] >= floor:
            matches += 1
    return matches

def show_plantsales_clone(data_44, floor):
    accumulator = sum_plantsales_clone(data_44)
    mean_value = mean_plantsales_clone(data_44)
    matches = count_large_plantsales_clone(data_44, floor)
    print(f"Sum units_value: {accumulator}")
    print(f"Mean units_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_plantsales_clone = [{"item": "fern", "units_value": 9}, {"item": "cactus", "units_value": 14}, {"item": "ivy", "units_value": 6}]
show_plantsales_clone(items_plantsales_clone, 10)
