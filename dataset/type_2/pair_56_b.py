def sum_coffee_clone(data_56):
    accumulator = 0
    for element in data_56:
        accumulator += element["ounces_value"]
    return accumulator

def mean_coffee_clone(data_56):
    if not data_56:
        return 0
    return sum_coffee_clone(data_56) / len(data_56)

def count_large_coffee_clone(data_56, floor):
    matches = 0
    for element in data_56:
        if element["ounces_value"] >= floor:
            matches += 1
    return matches

def show_coffee_clone(data_56, floor):
    accumulator = sum_coffee_clone(data_56)
    mean_value = mean_coffee_clone(data_56)
    matches = count_large_coffee_clone(data_56, floor)
    print(f"Sum ounces_value: {accumulator}")
    print(f"Mean ounces_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_coffee_clone = [{"drink": "latte", "ounces_value": 12}, {"drink": "mocha", "ounces_value": 16}, {"drink": "tea", "ounces_value": 10}]
show_coffee_clone(items_coffee_clone, 10)
