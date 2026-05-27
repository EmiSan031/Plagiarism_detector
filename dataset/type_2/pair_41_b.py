def sum_markets_clone(data_41):
    accumulator = 0
    for element in data_41:
        accumulator += element["sales_value"]
    return accumulator

def mean_markets_clone(data_41):
    if not data_41:
        return 0
    return sum_markets_clone(data_41) / len(data_41)

def count_large_markets_clone(data_41, floor):
    matches = 0
    for element in data_41:
        if element["sales_value"] >= floor:
            matches += 1
    return matches

def show_markets_clone(data_41, floor):
    accumulator = sum_markets_clone(data_41)
    mean_value = mean_markets_clone(data_41)
    matches = count_large_markets_clone(data_41, floor)
    print(f"Sum sales_value: {accumulator}")
    print(f"Mean sales_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_markets_clone = [{"stand": "fruit", "sales_value": 230}, {"stand": "bread", "sales_value": 180}, {"stand": "juice", "sales_value": 205}]
show_markets_clone(items_markets_clone, 10)
