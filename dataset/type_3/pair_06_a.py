def max_value(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def min_value(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def range_spread(numbers):
    return max_value(numbers) - min_value(numbers)

def list_report(numbers):
    highest = max_value(numbers)
    lowest = min_value(numbers)
    spread = range_spread(numbers)
    total = 0
    for n in numbers:
        total += n
    count = len(numbers)
    print(f"Numbers         : {numbers}")
    print(f"Count           : {count}")
    print(f"Maximum         : {highest}")
    print(f"Minimum         : {lowest}")
    print(f"Spread          : {spread}")
    print(f"Sum             : {total}")
    print(f"Average         : {total / count:.2f}")

list_report([4, 9, 2, 15, 6])
