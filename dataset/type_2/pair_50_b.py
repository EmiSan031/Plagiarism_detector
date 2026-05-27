def sum_fuel_clone(data_50):
    accumulator = 0
    for element in data_50:
        accumulator += element["liters_value"]
    return accumulator

def mean_fuel_clone(data_50):
    if not data_50:
        return 0
    return sum_fuel_clone(data_50) / len(data_50)

def count_large_fuel_clone(data_50, floor):
    matches = 0
    for element in data_50:
        if element["liters_value"] >= floor:
            matches += 1
    return matches

def show_fuel_clone(data_50, floor):
    accumulator = sum_fuel_clone(data_50)
    mean_value = mean_fuel_clone(data_50)
    matches = count_large_fuel_clone(data_50, floor)
    print(f"Sum liters_value: {accumulator}")
    print(f"Mean liters_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_fuel_clone = [{"station": "A", "liters_value": 30}, {"station": "B", "liters_value": 22}, {"station": "C", "liters_value": 40}]
show_fuel_clone(items_fuel_clone, 10)
