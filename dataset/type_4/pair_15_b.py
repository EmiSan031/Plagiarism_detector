def filter_even(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


print(filter_even([1, 2, 3, 4, 5, 6]))
