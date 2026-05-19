# Sum all numbers in the list.
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Sum only positive numbers.
def sum_positive(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

# Sum only even numbers.
def sum_even(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
# Sum only odd numbers.
def sum_odd(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_numbers(sample))
print(sum_positive([-3, -1, 2, 4, 6]))
print(sum_even(sample))
print(sum_odd(sample))
