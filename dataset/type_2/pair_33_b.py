def sum_repairs_clone(data_33):
    accumulator = 0
    for element in data_33:
        accumulator += element["cost_value"]
    return accumulator

def mean_repairs_clone(data_33):
    if not data_33:
        return 0
    return sum_repairs_clone(data_33) / len(data_33)

def count_large_repairs_clone(data_33, floor):
    matches = 0
    for element in data_33:
        if element["cost_value"] >= floor:
            matches += 1
    return matches

def show_repairs_clone(data_33, floor):
    accumulator = sum_repairs_clone(data_33)
    mean_value = mean_repairs_clone(data_33)
    matches = count_large_repairs_clone(data_33, floor)
    print(f"Sum cost_value: {accumulator}")
    print(f"Mean cost_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_repairs_clone = [{"id": "R1", "cost_value": 45}, {"id": "R2", "cost_value": 80}, {"id": "R3", "cost_value": 25}]
show_repairs_clone(items_repairs_clone, 10)
