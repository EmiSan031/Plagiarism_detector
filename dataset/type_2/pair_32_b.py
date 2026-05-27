def sum_grades_clone(data_32):
    accumulator = 0
    for element in data_32:
        accumulator += element["score_value"]
    return accumulator

def mean_grades_clone(data_32):
    if not data_32:
        return 0
    return sum_grades_clone(data_32) / len(data_32)

def count_large_grades_clone(data_32, floor):
    matches = 0
    for element in data_32:
        if element["score_value"] >= floor:
            matches += 1
    return matches

def show_grades_clone(data_32, floor):
    accumulator = sum_grades_clone(data_32)
    mean_value = mean_grades_clone(data_32)
    matches = count_large_grades_clone(data_32, floor)
    print(f"Sum score_value: {accumulator}")
    print(f"Mean score_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_grades_clone = [{"name": "Ana", "score_value": 91}, {"name": "Luis", "score_value": 78}, {"name": "Mia", "score_value": 86}]
show_grades_clone(items_grades_clone, 10)
