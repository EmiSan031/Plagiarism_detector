def fibonacci(n):
    def value_at(index):
        if index <= 1:
            return index
        return value_at(index - 1) + value_at(index - 2)
    return [value_at(pos) for pos in range(n)]

def fibonacci_at(n):
    def value_at(index):
        if index <= 1:
            return index
        return value_at(index - 1) + value_at(index - 2)
    return value_at(n)

def fibonacci_sum(n):
    return sum(fibonacci(n))

def is_fibonacci(n):
    return n in fibonacci(20)

print(fibonacci(8))
print(fibonacci_at(10))
print(fibonacci_sum(8))
print(is_fibonacci(13))
print(is_fibonacci(14))
