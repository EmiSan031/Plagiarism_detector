def largest_element(values):
    biggest = values[0]
    for current in values:
        if current > biggest:
            biggest = current
    return biggest

def smallest_element(values):
    tiniest = values[0]
    for current in values:
        if current < tiniest:
            tiniest = current
    return tiniest

def summarize_collection(values):
    if not values:
        print("The collection is empty.")
        return
    peak = largest_element(values)
    floor = smallest_element(values)
    grand_total = sum(values)
    qty = len(values)
    mean = grand_total / qty
    gap = peak - floor
    print(f"Collection      : {values}")
    print(f"Largest element : {peak}")
    print(f"Smallest element: {floor}")
    print(f"Total sum       : {grand_total}")
    print(f"Element count   : {qty}")
    print(f"Mean value      : {mean:.2f}")
    print(f"Value gap       : {gap}")

summarize_collection([10, 3, 22, 5, 11])
