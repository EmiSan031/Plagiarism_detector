def sum_supplies_clone(data_60):
    accumulator = 0
    for element in data_60:
        accumulator += element["items_value"]
    return accumulator

def mean_supplies_clone(data_60):
    if not data_60:
        return 0
    return sum_supplies_clone(data_60) / len(data_60)

def count_large_supplies_clone(data_60, floor):
    matches = 0
    for element in data_60:
        if element["items_value"] >= floor:
            matches += 1
    return matches

def show_supplies_clone(data_60, floor):
    accumulator = sum_supplies_clone(data_60)
    mean_value = mean_supplies_clone(data_60)
    matches = count_large_supplies_clone(data_60, floor)
    print(f"Sum items_value: {accumulator}")
    print(f"Mean items_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_supplies_clone = [{"box": "red", "items_value": 15}, {"box": "blue", "items_value": 22}, {"box": "green", "items_value": 11}]
show_supplies_clone(items_supplies_clone, 10)
