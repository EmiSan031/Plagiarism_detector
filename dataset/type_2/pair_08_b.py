def build_series(size):
    values = []
    first = 0
    second = 1
    for _ in range(size):
        values.append(first)
        first, second = second, first + second
    return values


print(build_series(6))
