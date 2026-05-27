def sum_patients_clone(data_34):
    accumulator = 0
    for element in data_34:
        accumulator += element["age_value"]
    return accumulator

def mean_patients_clone(data_34):
    if not data_34:
        return 0
    return sum_patients_clone(data_34) / len(data_34)

def count_large_patients_clone(data_34, floor):
    matches = 0
    for element in data_34:
        if element["age_value"] >= floor:
            matches += 1
    return matches

def show_patients_clone(data_34, floor):
    accumulator = sum_patients_clone(data_34)
    mean_value = mean_patients_clone(data_34)
    matches = count_large_patients_clone(data_34, floor)
    print(f"Sum age_value: {accumulator}")
    print(f"Mean age_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_patients_clone = [{"name": "Iris", "age_value": 34}, {"name": "Noe", "age_value": 52}, {"name": "Leo", "age_value": 29}]
show_patients_clone(items_patients_clone, 10)
