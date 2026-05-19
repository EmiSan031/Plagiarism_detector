def remove_duplicates(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result

def count_duplicates(values):
    unique = remove_duplicates(values)
    duplicates = 0
    for value in values:
        count = 0
        for v in values:
            if v == value:
                count += 1
        if count > 1:
            duplicates += 1
    return duplicates // 2 if duplicates > 0 else 0

def duplicate_report(values):
    if not values:
        print("The list is empty.")
        return
    unique = remove_duplicates(values)
    print(f"Original list   : {values}")
    print(f"Original length : {len(values)}")
    print(f"Unique values   : {unique}")
    print(f"Unique count    : {len(unique)}")
    removed = len(values) - len(unique)
    print(f"Duplicates removed: {removed}")
    for val in unique:
        freq = 0
        for v in values:
            if v == val:
                freq += 1
        if freq > 1:
            print(f"  '{val}' appeared {freq} times")

duplicate_report([1, 2, 1, 3, 2, 4])
