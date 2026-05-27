def sum_mileage_clone(data_59):
    accumulator = 0
    for element in data_59:
        accumulator += element["kilometers_value"]
    return accumulator

def mean_mileage_clone(data_59):
    if not data_59:
        return 0
    return sum_mileage_clone(data_59) / len(data_59)

def count_large_mileage_clone(data_59, floor):
    matches = 0
    for element in data_59:
        if element["kilometers_value"] >= floor:
            matches += 1
    return matches

def show_mileage_clone(data_59, floor):
    accumulator = sum_mileage_clone(data_59)
    mean_value = mean_mileage_clone(data_59)
    matches = count_large_mileage_clone(data_59, floor)
    print(f"Sum kilometers_value: {accumulator}")
    print(f"Mean kilometers_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_mileage_clone = [{"car": "sedan", "kilometers_value": 240}, {"car": "van", "kilometers_value": 180}, {"car": "truck", "kilometers_value": 310}]
show_mileage_clone(items_mileage_clone, 10)
