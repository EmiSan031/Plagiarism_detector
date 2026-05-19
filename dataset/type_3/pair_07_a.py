def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def highest_score(numbers):
    best = numbers[0]
    for number in numbers:
        if number > best:
            best = number
    return best

def lowest_score(numbers):
    worst = numbers[0]
    for number in numbers:
        if number < worst:
            worst = number
    return worst

def grade_report(numbers):
    avg = average(numbers)
    best = highest_score(numbers)
    worst = lowest_score(numbers)
    count = len(numbers)
    print(f"Grades          : {numbers}")
    print(f"Count           : {count}")
    print(f"Average         : {avg:.2f}")
    print(f"Highest         : {best}")
    print(f"Lowest          : {worst}")
    if avg >= 9:
        print(f"Status          : Excellent")
    elif avg >= 7:
        print(f"Status          : Good")
    else:
        print(f"Status          : Needs improvement")

grade_report([10, 8, 9, 7])
