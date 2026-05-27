def sum_bakerysales_clone(data_55):
    accumulator = 0
    for element in data_55:
        accumulator += element["sold_value"]
    return accumulator

def mean_bakerysales_clone(data_55):
    if not data_55:
        return 0
    return sum_bakerysales_clone(data_55) / len(data_55)

def count_large_bakerysales_clone(data_55, floor):
    matches = 0
    for element in data_55:
        if element["sold_value"] >= floor:
            matches += 1
    return matches

def show_bakerysales_clone(data_55, floor):
    accumulator = sum_bakerysales_clone(data_55)
    mean_value = mean_bakerysales_clone(data_55)
    matches = count_large_bakerysales_clone(data_55, floor)
    print(f"Sum sold_value: {accumulator}")
    print(f"Mean sold_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_bakerysales_clone = [{"batch": "am", "sold_value": 54}, {"batch": "pm", "sold_value": 61}, {"batch": "eve", "sold_value": 42}]
show_bakerysales_clone(items_bakerysales_clone, 10)
