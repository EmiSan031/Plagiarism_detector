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


print(order_list([5, 1, 4, 2, 8]))
