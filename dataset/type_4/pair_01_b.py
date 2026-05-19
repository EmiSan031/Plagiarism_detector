def sum_numbers(numbers):
    return sum(numbers)

def sum_positive(numbers):
    return sum(n for n in numbers if n > 0)

def sum_even(numbers):
    return sum(filter(lambda n: n % 2 == 0, numbers))

def sum_odd(numbers):
    return sum(filter(lambda n: n % 2 != 0, numbers))

def sum_squares(numbers):
    return sum(n ** 2 for n in numbers)

def sum_above(numbers, threshold):
    return sum(n for n in numbers if n > threshold)

def weighted_sum(numbers, weights):
    return sum(n * w for n, w in zip(numbers, weights))

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_numbers(sample))
print(sum_positive([-3, -1, 2, 4, 6]))
print(sum_even(sample))
print(sum_odd(sample))
print(sum_squares([1, 2, 3]))
print(sum_above(sample, 5))
print(weighted_sum([1, 2, 3], [1, 2, 3]))
