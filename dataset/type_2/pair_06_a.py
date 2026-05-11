def max_value(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


print(max_value([4, 9, 2, 15, 6]))
