def split_even_odd(values):
    even = []
    odd = []
    for value in values:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    return even, odd

print(split_even_odd([1, 2, 3, 4, 5]))
