def sum_calls_clone(data_38):
    accumulator = 0
    for element in data_38:
        accumulator += element["minutes_value"]
    return accumulator

def mean_calls_clone(data_38):
    if not data_38:
        return 0
    return sum_calls_clone(data_38) / len(data_38)

def count_large_calls_clone(data_38, floor):
    matches = 0
    for element in data_38:
        if element["minutes_value"] >= floor:
            matches += 1
    return matches

def show_calls_clone(data_38, floor):
    accumulator = sum_calls_clone(data_38)
    mean_value = mean_calls_clone(data_38)
    matches = count_large_calls_clone(data_38, floor)
    print(f"Sum minutes_value: {accumulator}")
    print(f"Mean minutes_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_calls_clone = [{"number": "111", "minutes_value": 5}, {"number": "222", "minutes_value": 11}, {"number": "333", "minutes_value": 2}]
show_calls_clone(items_calls_clone, 10)
