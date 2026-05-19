def max_value(numbers):
    return max(numbers)

def min_value(numbers):
    return min(numbers)

def value_range(numbers):
    return max(numbers) - min(numbers)

def second_max(numbers):
    unique_sorted = sorted(set(numbers), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def clamp(value, low, high):
    return max(low, min(high, value))

def normalize(numbers):
    lo, hi = min(numbers), max(numbers)
    return [(x - lo) / (hi - lo) for x in numbers]

def top_n(numbers, n):
    return sorted(set(numbers), reverse=True)[:n]

data = [4, 9, 2, 15, 6, 11, 3, 7]
print(max_value(data))
print(min_value(data))
print(value_range(data))
print(second_max(data))
print(clamp(20, 0, 10))
print(normalize([0, 5, 10]))
print(top_n(data, 3))
