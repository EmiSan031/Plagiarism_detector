def average(numbers):
    return sum(numbers) / len(numbers)

def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((n - mean) ** 2 for n in numbers) / len(numbers)

def std_deviation(numbers):
    return variance(numbers) ** 0.5

def median(numbers):
    s = sorted(numbers)
    mid = len(s) // 2
    return (s[mid - 1] + s[mid]) / 2 if len(s) % 2 == 0 else s[mid]

data = [10, 8, 9, 7, 6, 5, 4, 3]
print(average(data))
print(variance(data))
print(std_deviation(data))
print(median(data))
