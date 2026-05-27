def second_largest(values):
    first = second = None
    for value in values:
        if first is None or value > first:
            second = first
            first = value
        elif second is None or (value > second and value != first):
            second = value
    return second

def top_two(values):
    first = second_largest(values)
    maximum = max(values)
    return maximum, first

def ranking_report(values):
    maximum, second = top_two(values)
    print(f"List            : {values}")
    print(f"Count           : {len(values)}")
    print(f"Largest         : {maximum}")
    print(f"Second largest  : {second}")
    if second is None:
        print(f"Note            : No distinct second value.")
    else:
        print(f"Difference      : {maximum - second}")
    total = 0
    for v in values:
        total += v
    print(f"Sum             : {total}")
    return second

ranking_report([4, 1, 9, 3, 9, 7, 2])
