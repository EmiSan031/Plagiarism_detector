def common_divisor(first, second):
    while second != 0:
        rest = first % second
        first = second
        second = rest
    return first


print(common_divisor(96, 36))
