def linear_search(values, target):
    # Return the first matching index.
    for index in range(len(values)):
        if values[index] == target:
            return index

    return -1


print(linear_search([3, 6, 9, 12], 9))
