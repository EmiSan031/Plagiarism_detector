def largest_element(values):
    if len(values) == 0:
        return None
    biggest = values[0]
    changes = 0
    for current in values:
        if current > biggest:
            biggest = current
            changes += 1
    return biggest

def smallest_element(values):
    if len(values) == 0:
        return None
    tiniest = values[0]
    for current in values:
        if current < tiniest:
            tiniest = current
    return tiniest

def value_spread(values):
    if len(values) == 0:
        return None
    return largest_element(values) - smallest_element(values)

def collection_report(values):
    if len(values) == 0:
        print("Collection is empty.")
        return
    peak = largest_element(values)
    floor = smallest_element(values)
    gap = value_spread(values)
    grand_total = 0
    for v in values:
        grand_total += v
    qty = len(values)
    print(f"Collection      : {values}")
    print(f"Count           : {qty}")
    print(f"Largest         : {peak}")
    print(f"Smallest        : {floor}")
    print(f"Spread          : {gap}")
    print(f"Total           : {grand_total}")
    print(f"Mean            : {grand_total / qty:.2f}")

collection_report([4, 9, 2, 15, 6])
