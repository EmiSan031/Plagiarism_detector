def find_position(items, expected):
    for position in range(len(items)):
        if items[position] == expected:
            return position
    return -1

def tally_matches(items, expected):
    matches = 0
    for entry in items:
        if entry == expected:
            matches += 1
    return matches

def lookup_report(items, expected):
    location = find_position(items, expected)
    matches = tally_matches(items, expected)
    print(f"Collection      : {items}")
    print(f"Value sought    : {expected}")
    print(f"Collection size : {len(items)}")
    if location != -1:
        print(f"Located at index: {location}")
        print(f"Stored value    : {items[location]}")
    else:
        print(f"Value {expected} was NOT found in the collection.")
    print(f"Match count     : {matches}")
    for idx, entry in enumerate(items):
        marker = "<-- match" if entry == expected else ""
        print(f"  index {idx}: {entry} {marker}")

lookup_report([2, 4, 6, 8], 6)
