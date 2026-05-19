def build_series(size):
    values = []
    first = 0
    second = 1
    for _ in range(size):
        values.append(first)
        first, second = second, first + second
    return values

def belongs_to_series(entry):
    reference = build_series(50)
    return entry in reference

def display_series_report(size):
    values = build_series(size)
    print(f"Generated series ({size} terms): {values}")
    print(f"Opening term : {values[0]}")
    print(f"Closing term : {values[-1]}")
    running_total = 0
    for item in values:
        running_total += item
    print(f"Cumulative sum: {running_total}")
    even_items = 0
    for item in values:
        if item % 2 == 0:
            even_items += 1
    print(f"Even entries in series: {even_items}")
    print(f"Does 21 belong to the series? {belongs_to_series(21)}")
    print(f"Does 22 belong to the series? {belongs_to_series(22)}")

display_series_report(6)
