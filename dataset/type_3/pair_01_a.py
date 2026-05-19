def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def get_stats(numbers):
    total = sum_numbers(numbers)
    count = len(numbers)
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return total, count, minimum, maximum

def print_summary(numbers):
    total, count, minimum, maximum = get_stats(numbers)
    print(f"Numbers         : {numbers}")
    print(f"Count           : {count}")
    print(f"Sum             : {total}")
    print(f"Minimum         : {minimum}")
    print(f"Maximum         : {maximum}")
    print(f"Average         : {total / count:.2f}")
    return total

sample = [1, 2, 3, 4, 5]
result = print_summary(sample)
print(f"Final sum: {result}")
