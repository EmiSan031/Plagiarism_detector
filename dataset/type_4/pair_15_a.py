def filter_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

def filter_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result

def filter_positive(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result

def filter_greater_than(numbers, threshold):
    result = []
    for number in numbers:
        if number > threshold:
            result.append(number)
    return result

data = [1, -2, 3, -4, 5, 6, -7, 8]
print(filter_even(data))
print(filter_odd(data))
print(filter_positive(data))
print(filter_greater_than(data, 3))
