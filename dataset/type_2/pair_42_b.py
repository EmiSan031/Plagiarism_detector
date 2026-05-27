def sum_trips_clone(data_42):
    accumulator = 0
    for element in data_42:
        accumulator += element["days_value"]
    return accumulator

def mean_trips_clone(data_42):
    if not data_42:
        return 0
    return sum_trips_clone(data_42) / len(data_42)

def count_large_trips_clone(data_42, floor):
    matches = 0
    for element in data_42:
        if element["days_value"] >= floor:
            matches += 1
    return matches

def show_trips_clone(data_42, floor):
    accumulator = sum_trips_clone(data_42)
    mean_value = mean_trips_clone(data_42)
    matches = count_large_trips_clone(data_42, floor)
    print(f"Sum days_value: {accumulator}")
    print(f"Mean days_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_trips_clone = [{"city": "A", "days_value": 3}, {"city": "B", "days_value": 5}, {"city": "C", "days_value": 2}]
show_trips_clone(items_trips_clone, 10)
