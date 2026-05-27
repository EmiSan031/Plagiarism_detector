def sum_workouts_clone(data_47):
    accumulator = 0
    for element in data_47:
        accumulator += element["reps_value"]
    return accumulator

def mean_workouts_clone(data_47):
    if not data_47:
        return 0
    return sum_workouts_clone(data_47) / len(data_47)

def count_large_workouts_clone(data_47, floor):
    matches = 0
    for element in data_47:
        if element["reps_value"] >= floor:
            matches += 1
    return matches

def show_workouts_clone(data_47, floor):
    accumulator = sum_workouts_clone(data_47)
    mean_value = mean_workouts_clone(data_47)
    matches = count_large_workouts_clone(data_47, floor)
    print(f"Sum reps_value: {accumulator}")
    print(f"Mean reps_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_workouts_clone = [{"move": "push", "reps_value": 20}, {"move": "squat", "reps_value": 30}, {"move": "row", "reps_value": 18}]
show_workouts_clone(items_workouts_clone, 10)
