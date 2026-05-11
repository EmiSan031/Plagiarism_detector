def add_values(data):
    if not data:
        return 0
    accumulator = 0
    for item in data:
        accumulator += item
    print("items:", len(data))
    return accumulator


print(add_values([1, 2, 3, 4, 5]))
