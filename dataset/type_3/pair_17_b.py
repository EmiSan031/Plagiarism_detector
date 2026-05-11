def common_divisor(first, second):
    first = abs(first)
    second = abs(second)
    steps = 0
    while second != 0:
        rest = first % second
        first = second
        second = rest
        steps += 1
    print("steps:", steps)
    return first


print(common_divisor(84, 30))
