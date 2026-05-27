def sum_storage_clone(data_57):
    accumulator = 0
    for element in data_57:
        accumulator += element["gigabytes_value"]
    return accumulator

def mean_storage_clone(data_57):
    if not data_57:
        return 0
    return sum_storage_clone(data_57) / len(data_57)

def count_large_storage_clone(data_57, floor):
    matches = 0
    for element in data_57:
        if element["gigabytes_value"] >= floor:
            matches += 1
    return matches

def show_storage_clone(data_57, floor):
    accumulator = sum_storage_clone(data_57)
    mean_value = mean_storage_clone(data_57)
    matches = count_large_storage_clone(data_57, floor)
    print(f"Sum gigabytes_value: {accumulator}")
    print(f"Mean gigabytes_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_storage_clone = [{"drive": "A", "gigabytes_value": 512}, {"drive": "B", "gigabytes_value": 256}, {"drive": "C", "gigabytes_value": 1024}]
show_storage_clone(items_storage_clone, 10)
