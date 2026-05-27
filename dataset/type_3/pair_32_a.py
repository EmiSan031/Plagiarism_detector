def powers_of_two(n):
    result = []
    for i in range(n + 1):
        value = 1
        for _ in range(i):
            value *= 2
        result.append(value)
    return result

def sum_powers(n):
    total = 0
    for val in powers_of_two(n):
        total += val
    return total

def powers_report(n):
    sequence = powers_of_two(n)
    print(f"Powers of 2 up to 2^{n}:")
    for i, val in enumerate(sequence):
        print(f"  2^{i} = {val}")
    print(f"Total terms     : {len(sequence)}")
    print(f"Sum of all      : {sum_powers(n)}")
    print(f"Largest value   : {sequence[-1]}")
    return sequence

powers_report(8)
