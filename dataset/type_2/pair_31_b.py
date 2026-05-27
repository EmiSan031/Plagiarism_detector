def sum_orders_clone(data_31):
    accumulator = 0
    for element in data_31:
        accumulator += element["total_value"]
    return accumulator

def mean_orders_clone(data_31):
    if not data_31:
        return 0
    return sum_orders_clone(data_31) / len(data_31)

def count_large_orders_clone(data_31, floor):
    matches = 0
    for element in data_31:
        if element["total_value"] >= floor:
            matches += 1
    return matches

def show_orders_clone(data_31, floor):
    accumulator = sum_orders_clone(data_31)
    mean_value = mean_orders_clone(data_31)
    matches = count_large_orders_clone(data_31, floor)
    print(f"Sum total_value: {accumulator}")
    print(f"Mean total_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_orders_clone = [{"id": 1, "total_value": 120}, {"id": 2, "total_value": 85}, {"id": 3, "total_value": 150}]
show_orders_clone(items_orders_clone, 10)
