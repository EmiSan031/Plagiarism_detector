def order_list(collection):
    copy = collection[:]
    for outer in range(len(copy)):
        for inner in range(0, len(copy) - outer - 1):
            if copy[inner] > copy[inner + 1]:
                copy[inner], copy[inner + 1] = copy[inner + 1], copy[inner]
    return copy


print(order_list([9, 3, 7, 1, 5]))
