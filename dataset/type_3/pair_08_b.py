def build_series(size):
    if size <= 0:
        return []
    values = []
    first = 0
    second = 1
    for _ in range(size):
        values.append(first)
        first, second = second, first + second
    last_value = values[-1]
    print("last:", last_value)
    return values

def belongs_to_series(num, size):
    return num in build_series(size)

def total_series(size):
    running = 0
    for val in build_series(size):
        running += val
    return running

def series_report(size):
    values = build_series(size)
    if not values:
        print(f"No terms generated for size {size}.")
        return values
    print(f"Terms requested : {size}")
    print(f"Series          : {values}")
    print(f"Opening term    : {values[0]}")
    print(f"Closing term    : {values[-1]}")
    print(f"Series total    : {total_series(size)}")
    even_count = sum(1 for v in values if v % 2 == 0)
    print(f"Even entries    : {even_count}")
    print(f"Is 13 in series?: {belongs_to_series(13, size)}")
    return values

series_report(8)
