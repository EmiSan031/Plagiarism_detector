def sum_plants_clone(data_35):
    accumulator = 0
    for element in data_35:
        accumulator += element["height_value"]
    return accumulator

def mean_plants_clone(data_35):
    if not data_35:
        return 0
    return sum_plants_clone(data_35) / len(data_35)

def count_large_plants_clone(data_35, floor):
    matches = 0
    for element in data_35:
        if element["height_value"] >= floor:
            matches += 1
    return matches

def show_plants_clone(data_35, floor):
    accumulator = sum_plants_clone(data_35)
    mean_value = mean_plants_clone(data_35)
    matches = count_large_plants_clone(data_35, floor)
    print(f"Sum height_value: {accumulator}")
    print(f"Mean height_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_plants_clone = [{"name": "basil", "height_value": 18}, {"name": "mint", "height_value": 12}, {"name": "rose", "height_value": 31}]
show_plants_clone(items_plants_clone, 10)
