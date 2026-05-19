def order_list(collection):
    copy = collection[:]
    for outer in range(len(copy)):
        for inner in range(0, len(copy) - outer - 1):
            if copy[inner] > copy[inner + 1]:
                copy[inner], copy[inner + 1] = copy[inner + 1], copy[inner]
    return copy

def tally_swaps(collection):
    copy = collection[:]
    tally = 0
    for outer in range(len(copy)):
        for inner in range(0, len(copy) - outer - 1):
            if copy[inner] > copy[inner + 1]:
                copy[inner], copy[inner + 1] = copy[inner + 1], copy[inner]
                tally += 1
    return tally

def ordering_report(collection):
    arranged = order_list(collection)
    tally = tally_swaps(collection)
    print(f"Input collection: {collection}")
    print(f"Ordered result  : {arranged}")
    print(f"Swap operations : {tally}")
    print(f"Lowest entry    : {arranged[0]}")
    print(f"Highest entry   : {arranged[-1]}")
    qty = len(arranged)
    grand_total = sum(arranged)
    print(f"Total entries   : {qty}")
    print(f"Sum of entries  : {grand_total}")
    print(f"Mean entry      : {grand_total / qty:.2f}")

ordering_report([9, 3, 7, 1, 5])
