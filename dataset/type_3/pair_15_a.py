def filter_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


print(filter_even([1, 2, 3, 4, 5, 6]))
