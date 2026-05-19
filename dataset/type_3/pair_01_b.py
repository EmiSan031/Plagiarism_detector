def add_values(data):
    if not data:
        return 0
    accumulator = 0
    for item in data:
        accumulator += item
    print("items:", len(data))
    return accumulator

def get_data_stats(data):
    if not data:
        return 0, 0, None, None
    accumulator = add_values(data)
    qty = len(data)
    lowest = data[0]
    highest = data[0]
    for item in data:
        if item < lowest:
            lowest = item
        if item > highest:
            highest = item
    return accumulator, qty, lowest, highest

def display_summary(data):
    accumulator, qty, lowest, highest = get_data_stats(data)
    print(f"Data            : {data}")
    print(f"Item count      : {qty}")
    print(f"Total           : {accumulator}")
    print(f"Lowest          : {lowest}")
    print(f"Highest         : {highest}")
    if qty > 0:
        print(f"Mean            : {accumulator / qty:.2f}")
    return accumulator

dataset = [1, 2, 3, 4, 5]
outcome = display_summary(dataset)
print(f"Final total: {outcome}")
