def sum_votes_clone(data_51):
    accumulator = 0
    for element in data_51:
        accumulator += element["votes_value"]
    return accumulator

def mean_votes_clone(data_51):
    if not data_51:
        return 0
    return sum_votes_clone(data_51) / len(data_51)

def count_large_votes_clone(data_51, floor):
    matches = 0
    for element in data_51:
        if element["votes_value"] >= floor:
            matches += 1
    return matches

def show_votes_clone(data_51, floor):
    accumulator = sum_votes_clone(data_51)
    mean_value = mean_votes_clone(data_51)
    matches = count_large_votes_clone(data_51, floor)
    print(f"Sum votes_value: {accumulator}")
    print(f"Mean votes_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_votes_clone = [{"zone": "N", "votes_value": 320}, {"zone": "S", "votes_value": 280}, {"zone": "E", "votes_value": 410}]
show_votes_clone(items_votes_clone, 10)
