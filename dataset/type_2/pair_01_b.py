# Computes the total of a collection of numeric data
def add_values(data):
    accumulator = 0
    if not data:
        print("Collection is empty, returning zero.")
        return 0
    for item in data:
        if not isinstance(item, (int, float)):
            print(f"Ignoring invalid entry: {item}")
            continue
        accumulator += item
    return accumulator

def display_report(data):
    accumulator = add_values(data)
    qty = len(data)
    print(f"Input collection: {data}")
    print(f"Number of entries: {qty}")
    print(f"Accumulated total: {accumulator}")
    if qty > 0:
        print(f"Mean value: {accumulator / qty:.2f}")
    else:
        print("Collection has no valid entries for mean calculation.")
    return accumulator

dataset = [6, 7, 8, 9, 10]
outcome = display_report(dataset)
print(f"Returned value: {outcome}")
