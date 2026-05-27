def mean(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)

def variance(values):
    avg = mean(values)
    total = 0
    for v in values:
        total += (v - avg) ** 2
    return total / len(values)

def std_deviation(values):
    var = variance(values)
    result = var ** 0.5
    return result

def stats_report(values):
    avg = mean(values)
    var = variance(values)
    std = std_deviation(values)
    print(f"Values          : {values}")
    print(f"Count           : {len(values)}")
    print(f"Mean            : {avg:.4f}")
    print(f"Variance        : {var:.4f}")
    print(f"Std deviation   : {std:.4f}")
    print(f"Min             : {min(values)}")
    print(f"Max             : {max(values)}")
    return avg, var, std

stats_report([4, 8, 15, 16, 23, 42])
