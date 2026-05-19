def max_value(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum  # Expected: 15

def min_value(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

# Difference between the largest and smallest value.
def value_range(numbers):
    return max_value(numbers) - min_value(numbers)

def second_max(numbers):
    first = max_value(numbers)
    second = None
    for number in numbers:
        if number != first:
            if second is None or number > second:
                second = number
    return second

data = [4, 9, 2, 15, 6, 11, 3, 7]
print(max_value(data))
print(min_value(data))
print(value_range(data))
print(second_max(data))
