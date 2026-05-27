def sum_laundry_clone(data_46):
    accumulator = 0
    for element in data_46:
        accumulator += element["pounds_value"]
    return accumulator

def mean_laundry_clone(data_46):
    if not data_46:
        return 0
    return sum_laundry_clone(data_46) / len(data_46)

def count_large_laundry_clone(data_46, floor):
    matches = 0
    for element in data_46:
        if element["pounds_value"] >= floor:
            matches += 1
    return matches

def show_laundry_clone(data_46, floor):
    accumulator = sum_laundry_clone(data_46)
    mean_value = mean_laundry_clone(data_46)
    matches = count_large_laundry_clone(data_46, floor)
    print(f"Sum pounds_value: {accumulator}")
    print(f"Mean pounds_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_laundry_clone = [{"load": "white", "pounds_value": 9}, {"load": "color", "pounds_value": 12}, {"load": "linen", "pounds_value": 7}]
show_laundry_clone(items_laundry_clone, 10)
