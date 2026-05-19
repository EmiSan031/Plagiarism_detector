def order_list(collection):
    copy = collection[:]
    swaps = 0
    for outer in range(len(copy)):
        changed = False
        for inner in range(0, len(copy) - outer - 1):
            if copy[inner] > copy[inner + 1]:
                copy[inner], copy[inner + 1] = copy[inner + 1], copy[inner]
                swaps += 1
                changed = True
        if not changed:
            break
    print("swaps:", swaps)
    return copy

def check_ordered(collection):
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            return False
    return True

def ordering_report(collection):
    print(f"Original        : {collection}")
    print(f"Already ordered : {check_ordered(collection)}")
    arranged = order_list(collection)
    print(f"Ordered result  : {arranged}")
    print(f"Verified ordered: {check_ordered(arranged)}")
    running = 0
    for v in arranged:
        running += v
    qty = len(arranged)
    print(f"Lowest entry    : {arranged[0]}")
    print(f"Highest entry   : {arranged[-1]}")
    print(f"Total           : {running}")
    print(f"Mean            : {running / qty:.2f}")

ordering_report([5, 1, 4, 2, 8])
