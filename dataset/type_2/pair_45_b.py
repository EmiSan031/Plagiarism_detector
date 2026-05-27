def sum_downloads_clone(data_45):
    accumulator = 0
    for element in data_45:
        accumulator += element["downloads_value"]
    return accumulator

def mean_downloads_clone(data_45):
    if not data_45:
        return 0
    return sum_downloads_clone(data_45) / len(data_45)

def count_large_downloads_clone(data_45, floor):
    matches = 0
    for element in data_45:
        if element["downloads_value"] >= floor:
            matches += 1
    return matches

def show_downloads_clone(data_45, floor):
    accumulator = sum_downloads_clone(data_45)
    mean_value = mean_downloads_clone(data_45)
    matches = count_large_downloads_clone(data_45, floor)
    print(f"Sum downloads_value: {accumulator}")
    print(f"Mean downloads_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_downloads_clone = [{"file": "app", "downloads_value": 120}, {"file": "doc", "downloads_value": 42}, {"file": "img", "downloads_value": 75}]
show_downloads_clone(items_downloads_clone, 10)
