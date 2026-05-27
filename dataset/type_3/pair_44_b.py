def build_tribonacci(size):
    if size < 0:
        return []
    if size == 0:
        return []
    if size == 1:
        return [0]
    if size == 2:
        return [0, 0]
    series = [0, 0, 1]
    for _ in range(3, size):
        upcoming = series[-1] + series[-2] + series[-3]
        series.append(upcoming)
    return series[:size]

def tribonacci_total(size):
    running = 0
    for entry in build_tribonacci(size):
        running += entry
    return running

def is_tribonacci(num, size):
    return num in build_tribonacci(size)

def series_report(size):
    if size < 0:
        print(f"Invalid size: {size}")
        return []
    series = build_tribonacci(size)
    running = tribonacci_total(size)
    print(f"Terms requested : {size}")
    print(f"Series          : {series}")
    print(f"Closing term    : {series[-1] if series else 'N/A'}")
    print(f"Cumulative sum  : {running}")
    even_tally = sum(1 for v in series if v % 2 == 0)
    print(f"Even entries    : {even_tally}")
    print(f"Odd entries     : {size - even_tally}")
    print(f"Is 7 in series? : {is_tribonacci(7, size)}")
    return series

series_report(10)
