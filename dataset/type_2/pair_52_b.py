def sum_ticketsales_clone(data_52):
    accumulator = 0
    for element in data_52:
        accumulator += element["tickets_value"]
    return accumulator

def mean_ticketsales_clone(data_52):
    if not data_52:
        return 0
    return sum_ticketsales_clone(data_52) / len(data_52)

def count_large_ticketsales_clone(data_52, floor):
    matches = 0
    for element in data_52:
        if element["tickets_value"] >= floor:
            matches += 1
    return matches

def show_ticketsales_clone(data_52, floor):
    accumulator = sum_ticketsales_clone(data_52)
    mean_value = mean_ticketsales_clone(data_52)
    matches = count_large_ticketsales_clone(data_52, floor)
    print(f"Sum tickets_value: {accumulator}")
    print(f"Mean tickets_value: {mean_value:.2f}")
    print(f"Matching records: {matches}")
    return accumulator, mean_value, matches

items_ticketsales_clone = [{"show": "one", "tickets_value": 80}, {"show": "two", "tickets_value": 65}, {"show": "three", "tickets_value": 92}]
show_ticketsales_clone(items_ticketsales_clone, 10)
