def sum_badges_clone(data_43):
    accumulator = 0
    for element in data_43:
        accumulator += element["badges_value"]
    return accumulator

def mean_badges_clone(data_43):
    if not data_43:
        return 0
    return sum_badges_clone(data_43) / len(data_43)

def count_large_badges_clone(data_43, floor):
    matches = 0
    for element in data_43:
        if element["badges_value"] >= floor:
            matches += 1
    return matches

def show_badges_clone(data_43, floor):
    accumulator = sum_badges_clone(data_43)
    mean_value = mean_badges_clone(data_43)
    matches = count_large_badges_clone(data_43, floor)
    print(f"Sum badges_value: {accumulator}")
    print(f"Mean badges_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_badges_clone = [{"name": "Paz", "badges_value": 4}, {"name": "Sol", "badges_value": 7}, {"name": "Rui", "badges_value": 3}]
show_badges_clone(items_badges_clone, 10)
