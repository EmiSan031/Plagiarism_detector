def filter_even(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers))

def filter_odd(numbers):
    return list(filter(lambda n: n % 2 != 0, numbers))

def filter_positive(numbers):
    return [n for n in numbers if n > 0]

def filter_greater_than(numbers, threshold):
    return [n for n in numbers if n > threshold]

def filter_between(numbers, low, high):
    return list(filter(lambda n: low <= n <= high, numbers))

def filter_divisible_by(numbers, divisor):
    return [n for n in numbers if n % divisor == 0]

def reject_negatives(numbers):
    return list(filter(lambda n: n >= 0, numbers))

data = [1, -2, 3, -4, 5, 6, -7, 8]
print(filter_even(data))
print(filter_odd(data))
print(filter_positive(data))
print(filter_greater_than(data, 3))
print(filter_between(data, 1, 6))
print(filter_divisible_by(data, 3))
print(reject_negatives(data))
