def check_ascending(collection):
    if len(collection) == 0:
        return True
    for idx in range(len(collection) - 1):
        if collection[idx] > collection[idx + 1]:
            return False
    return True

def count_inversions(collection):
    inversions = 0
    for idx in range(len(collection) - 1):
        if collection[idx] > collection[idx + 1]:
            inversions += 1
    return inversions

def first_disorder(collection):
    for idx in range(len(collection) - 1):
        if collection[idx] > collection[idx + 1]:
            return idx
    return -1

def order_report(collection):
    if len(collection) == 0:
        print("Collection is empty.")
        return True
    outcome = check_ascending(collection)
    disorder_idx = first_disorder(collection)
    inversions = count_inversions(collection)
    print(f"Collection      : {collection}")
    print(f"Size            : {len(collection)}")
    print(f"Is ascending    : {outcome}")
    print(f"Inversions found: {inversions}")
    if not outcome:
        print(f"First disorder  : index {disorder_idx} (value {collection[disorder_idx]})")
    else:
        print(f"All elements in ascending order.")
    return outcome

order_report([1, 3, 5, 7, 9])
print()
order_report([1, 5, 3, 7, 9])
