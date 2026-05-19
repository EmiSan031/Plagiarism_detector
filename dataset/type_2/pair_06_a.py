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

def analyze_list(numbers):
    if not numbers:
        print("The list is empty.")
        return
    highest = max_value(numbers)
    lowest = min_value(numbers)
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    spread = highest - lowest
    print(f"Numbers         : {numbers}")
    print(f"Maximum value   : {highest}")
    print(f"Minimum value   : {lowest}")
    print(f"Sum             : {total}")
    print(f"Count           : {count}")
    print(f"Average         : {average:.2f}")
    print(f"Range (spread)  : {spread}")

analyze_list([4, 9, 2, 15, 6])
