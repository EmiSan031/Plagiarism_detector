def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average([10, 8, 9, 7]))
