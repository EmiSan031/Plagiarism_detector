def sum_numbers(numbers):
    total = 0
    if not numbers:
        print("The list is empty, returning 0.")
        return 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            print(f"Skipping non-numeric value: {number}")
            continue
        total += number
    return total

def print_summary(numbers):
    total = sum_numbers(numbers)
    count = len(numbers)
    print(f"List of numbers: {numbers}")
    print(f"Total elements: {count}")
    print(f"Sum of all numbers: {total}")
    if count > 0:
        print(f"Average value: {total / count:.2f}")
    else:
        print("No valid elements to compute average.")
    return total

sample_list = [1, 2, 3, 4, 5]
result = print_summary(sample_list)
print(f"Final result: {result}")
