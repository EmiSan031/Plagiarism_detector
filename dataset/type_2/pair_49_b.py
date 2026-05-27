def sum_printing_clone(data_49):
    accumulator = 0
    for element in data_49:
        accumulator += element["pages_value"]
    return accumulator

def mean_printing_clone(data_49):
    if not data_49:
        return 0
    return sum_printing_clone(data_49) / len(data_49)

def count_large_printing_clone(data_49, floor):
    matches = 0
    for element in data_49:
        if element["pages_value"] >= floor:
            matches += 1
    return matches

def show_printing_clone(data_49, floor):
    accumulator = sum_printing_clone(data_49)
    mean_value = mean_printing_clone(data_49)
    matches = count_large_printing_clone(data_49, floor)
    print(f"Sum pages_value: {accumulator}")
    print(f"Mean pages_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_printing_clone = [{"job": "a", "pages_value": 10}, {"job": "b", "pages_value": 25}, {"job": "c", "pages_value": 6}]
show_printing_clone(items_printing_clone, 10)
