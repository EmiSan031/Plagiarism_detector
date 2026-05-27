def sum_rent_clone(data_37):
    accumulator = 0
    for element in data_37:
        accumulator += element["price_value"]
    return accumulator

def mean_rent_clone(data_37):
    if not data_37:
        return 0
    return sum_rent_clone(data_37) / len(data_37)

def count_large_rent_clone(data_37, floor):
    matches = 0
    for element in data_37:
        if element["price_value"] >= floor:
            matches += 1
    return matches

def show_rent_clone(data_37, floor):
    accumulator = sum_rent_clone(data_37)
    mean_value = mean_rent_clone(data_37)
    matches = count_large_rent_clone(data_37, floor)
    print(f"Sum price_value: {accumulator}")
    print(f"Mean price_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_rent_clone = [{"unit": "A", "price_value": 700}, {"unit": "B", "price_value": 820}, {"unit": "C", "price_value": 650}]
show_rent_clone(items_rent_clone, 10)
