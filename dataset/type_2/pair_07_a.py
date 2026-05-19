def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def get_highest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

def get_lowest(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest

def grade_report(numbers):
    avg = average(numbers)
    highest = get_highest(numbers)
    lowest = get_lowest(numbers)
    count = len(numbers)
    print(f"Grades          : {numbers}")
    print(f"Total grades    : {count}")
    print(f"Average grade   : {avg:.2f}")
    print(f"Highest grade   : {highest}")
    print(f"Lowest grade    : {lowest}")
    if avg >= 9:
        print("Performance     : Excellent")
    elif avg >= 7:
        print("Performance     : Good")
    else:
        print("Performance     : Needs Improvement")

grade_report([10, 8, 9, 7])
