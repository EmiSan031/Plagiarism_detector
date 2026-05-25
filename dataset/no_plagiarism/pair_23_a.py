def safe_divide(values, divisor):
    if divisor == 0:
        return []
    return [value / divisor for value in values]

print(safe_divide([10, 20, 30], 5))
