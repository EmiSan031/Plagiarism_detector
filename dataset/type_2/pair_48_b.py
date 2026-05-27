def sum_pets_clone(data_48):
    accumulator = 0
    for element in data_48:
        accumulator += element["weight_value"]
    return accumulator

def mean_pets_clone(data_48):
    if not data_48:
        return 0
    return sum_pets_clone(data_48) / len(data_48)

def count_large_pets_clone(data_48, floor):
    matches = 0
    for element in data_48:
        if element["weight_value"] >= floor:
            matches += 1
    return matches

def show_pets_clone(data_48, floor):
    accumulator = sum_pets_clone(data_48)
    mean_value = mean_pets_clone(data_48)
    matches = count_large_pets_clone(data_48, floor)
    print(f"Sum weight_value: {accumulator}")
    print(f"Mean weight_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_pets_clone = [{"name": "Luna", "weight_value": 8}, {"name": "Max", "weight_value": 12}, {"name": "Nox", "weight_value": 5}]
show_pets_clone(items_pets_clone, 10)
