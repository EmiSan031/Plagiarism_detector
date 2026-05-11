def fibonacci(n):
    def value_at(index):
        if index <= 1:
            return index
        return value_at(index - 1) + value_at(index - 2)

    return [value_at(position) for position in range(n)]


print(fibonacci(8))
