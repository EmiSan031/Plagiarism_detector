def unique_items(sequence):
    clean = []
    for element in sequence:
        if element not in clean:
            clean.append(element)
    return clean

def tally_repeated(sequence):
    distinct = unique_items(sequence)
    repeated = 0
    for element in sequence:
        tally = 0
        for e in sequence:
            if e == element:
                tally += 1
        if tally > 1:
            repeated += 1
    return repeated // 2 if repeated > 0 else 0

def uniqueness_report(sequence):
    if not sequence:
        print("The sequence is empty.")
        return
    distinct = unique_items(sequence)
    print(f"Input sequence  : {sequence}")
    print(f"Input length    : {len(sequence)}")
    print(f"Distinct items  : {distinct}")
    print(f"Distinct count  : {len(distinct)}")
    removed = len(sequence) - len(distinct)
    print(f"Entries removed : {removed}")
    for elem in distinct:
        freq = 0
        for e in sequence:
            if e == elem:
                freq += 1
        if freq > 1:
            print(f"  '{elem}' appeared {freq} times")

uniqueness_report([5, 6, 5, 7, 6, 8])
