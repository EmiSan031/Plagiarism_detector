def linear_search(values, target):
    try:
        return values.index(target)
    except ValueError:
        return -1


print(linear_search([3, 6, 9, 12], 9))
