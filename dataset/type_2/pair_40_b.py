def sum_lessons_clone(data_40):
    accumulator = 0
    for element in data_40:
        accumulator += element["minutes_value"]
    return accumulator

def mean_lessons_clone(data_40):
    if not data_40:
        return 0
    return sum_lessons_clone(data_40) / len(data_40)

def count_large_lessons_clone(data_40, floor):
    matches = 0
    for element in data_40:
        if element["minutes_value"] >= floor:
            matches += 1
    return matches

def show_lessons_clone(data_40, floor):
    accumulator = sum_lessons_clone(data_40)
    mean_value = mean_lessons_clone(data_40)
    matches = count_large_lessons_clone(data_40, floor)
    print(f"Sum minutes_value: {accumulator}")
    print(f"Mean minutes_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_lessons_clone = [{"topic": "math", "minutes_value": 45}, {"topic": "art", "minutes_value": 35}, {"topic": "music", "minutes_value": 40}]
show_lessons_clone(items_lessons_clone, 10)
