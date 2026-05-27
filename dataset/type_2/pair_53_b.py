def sum_cloud_clone(data_53):
    accumulator = 0
    for element in data_53:
        accumulator += element["load_value"]
    return accumulator

def mean_cloud_clone(data_53):
    if not data_53:
        return 0
    return sum_cloud_clone(data_53) / len(data_53)

def count_large_cloud_clone(data_53, floor):
    matches = 0
    for element in data_53:
        if element["load_value"] >= floor:
            matches += 1
    return matches

def show_cloud_clone(data_53, floor):
    accumulator = sum_cloud_clone(data_53)
    mean_value = mean_cloud_clone(data_53)
    matches = count_large_cloud_clone(data_53, floor)
    print(f"Sum load_value: {accumulator}")
    print(f"Mean load_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_cloud_clone = [{"host": "a", "load_value": 67}, {"host": "b", "load_value": 82}, {"host": "c", "load_value": 49}]
show_cloud_clone(items_cloud_clone, 10)
