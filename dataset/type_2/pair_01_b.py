# Same structure with renamed identifiers.
def add_values(data):
    accumulator = 0
    for item in data:
        accumulator += item
    return accumulator


print(add_values([6, 7, 8, 9, 10]))
