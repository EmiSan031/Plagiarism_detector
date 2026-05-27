def compute_mean(data):
    if len(data) == 0:
        return None
    running = 0
    for item in data:
        running += item
    return running / len(data)

def compute_variance(data):
    if len(data) == 0:
        return None
    avg = compute_mean(data)
    squared_diff = 0
    for item in data:
        squared_diff += (item - avg) ** 2
    return squared_diff / len(data)

def compute_std(data):
    if len(data) == 0:
        return None
    return compute_variance(data) ** 0.5

def dispersion_report(data):
    if len(data) == 0:
        print("Dataset is empty.")
        return None, None, None
    avg = compute_mean(data)
    var = compute_variance(data)
    std = compute_std(data)
    cv = (std / avg * 100) if avg != 0 else None
    print(f"Dataset         : {data}")
    print(f"Count           : {len(data)}")
    print(f"Mean            : {avg:.4f}")
    print(f"Variance        : {var:.4f}")
    print(f"Std deviation   : {std:.4f}")
    if cv is not None:
        print(f"Coeff variation : {cv:.2f}%")
    print(f"Min             : {min(data)}")
    print(f"Max             : {max(data)}")
    return avg, var, std

dispersion_report([4, 8, 15, 16, 23, 42])
