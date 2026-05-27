def sum_races_clone(data_36):
    accumulator = 0
    for element in data_36:
        accumulator += element["seconds_value"]
    return accumulator

def mean_races_clone(data_36):
    if not data_36:
        return 0
    return sum_races_clone(data_36) / len(data_36)

def count_large_races_clone(data_36, floor):
    matches = 0
    for element in data_36:
        if element["seconds_value"] >= floor:
            matches += 1
    return matches

def show_races_clone(data_36, floor):
    accumulator = sum_races_clone(data_36)
    mean_value = mean_races_clone(data_36)
    matches = count_large_races_clone(data_36, floor)
    print(f"Sum seconds_value: {accumulator}")
    print(f"Mean seconds_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_races_clone = [{"runner": "A", "seconds_value": 64}, {"runner": "B", "seconds_value": 59}, {"runner": "C", "seconds_value": 72}]
show_races_clone(items_races_clone, 10)
