def filter_even(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

def filter_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result

def even_odd_report(numbers):
    if not numbers:
        print("The list is empty.")
        return
    evens = filter_even(numbers)
    odds = filter_odd(numbers)
    print(f"Original list   : {numbers}")
    print(f"Total numbers   : {len(numbers)}")
    print(f"Even numbers    : {evens}")
    print(f"Count of evens  : {len(evens)}")
    print(f"Odd numbers     : {odds}")
    print(f"Count of odds   : {len(odds)}")
    even_sum = 0
    for n in evens:
        even_sum += n
    odd_sum = 0
    for n in odds:
        odd_sum += n
    print(f"Sum of evens    : {even_sum}")
    print(f"Sum of odds     : {odd_sum}")

even_odd_report([1, 2, 3, 4, 5, 6])
