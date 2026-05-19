def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def variance(numbers):
    mean = average(numbers)
    total = 0
    for number in numbers:
        total += (number - mean) ** 2
    return total / len(numbers)

def std_deviation(numbers):
    return variance(numbers) ** 0.5

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

data = [10, 8, 9, 7, 6, 5, 4, 3]
print(average(data))
print(variance(data))
print(std_deviation(data))
print(median(data))
