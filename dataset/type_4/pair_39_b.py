import itertools

def running_sum(numbers):
    return list(itertools.accumulate(numbers))

def running_max(numbers):
    return list(itertools.accumulate(numbers, max))

def running_product(numbers):
    import operator
    return list(itertools.accumulate(numbers, operator.mul))

def differences(numbers):
    return [b - a for a, b in zip(numbers, numbers[1:])]

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(running_sum(data))
print(running_max(data))
print(running_product([1, 2, 3, 4, 5]))
print(differences(data))
