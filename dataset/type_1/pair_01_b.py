# Sum all numbers in the list.
def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(sum_numbers([1, 2, 3, 4, 5]))
