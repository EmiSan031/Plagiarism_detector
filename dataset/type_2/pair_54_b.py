def sum_garden_clone(data_54):
    accumulator = 0
    for element in data_54:
        accumulator += element["plants_value"]
    return accumulator

def mean_garden_clone(data_54):
    if not data_54:
        return 0
    return sum_garden_clone(data_54) / len(data_54)

def count_large_garden_clone(data_54, floor):
    matches = 0
    for element in data_54:
        if element["plants_value"] >= floor:
            matches += 1
    return matches

def show_garden_clone(data_54, floor):
    accumulator = sum_garden_clone(data_54)
    mean_value = mean_garden_clone(data_54)
    matches = count_large_garden_clone(data_54, floor)
    print(f"Sum plants_value: {accumulator}")
    print(f"Mean plants_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_garden_clone = [{"bed": "A", "plants_value": 18}, {"bed": "B", "plants_value": 24}, {"bed": "C", "plants_value": 15}]
show_garden_clone(items_garden_clone, 10)
