def find_position(items, expected):
    if len(items) == 0:
        return -1
    checked = 0
    for position in range(len(items)):
        checked += 1
        if items[position] == expected:
            print("checked:", checked)
            return position
    return -1

def tally_matches(items, expected):
    matches = 0
    for entry in items:
        if entry == expected:
            matches += 1
    return matches

def lookup_report(items, expected):
    if len(items) == 0:
        print("Collection is empty.")
        return
    location = find_position(items, expected)
    matches = tally_matches(items, expected)
    print(f"Collection      : {items}")
    print(f"Target          : {expected}")
    print(f"Collection size : {len(items)}")
    if location != -1:
        print(f"Found at index  : {location}")
    else:
        print(f"Target not found in collection.")
    print(f"Match count     : {matches}")
    for idx, entry in enumerate(items):
        marker = " <-- match" if entry == expected else ""
        print(f"  [{idx}] {entry}{marker}")

lookup_report([3, 6, 9, 12], 9)
