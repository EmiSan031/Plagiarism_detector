def generate_base2(limit):
    if limit < 0:
        return []
    entries = []
    for exp in range(limit + 1):
        entry = 1
        for _ in range(exp):
            entry *= 2
        entries.append(entry)
    return entries

def accumulate_base2(limit):
    running = 0
    for entry in generate_base2(limit):
        running += entry
    return running

def base2_report(limit):
    if limit < 0:
        print(f"Invalid limit: {limit}")
        return []
    entries = generate_base2(limit)
    even_entries = []
    for e in entries:
        if e % 2 == 0:
            even_entries.append(e)
    print(f"Base-2 sequence up to 2^{limit}:")
    for exp, entry in enumerate(entries):
        print(f"  2^{exp} = {entry}")
    print(f"Total terms     : {len(entries)}")
    print(f"Cumulative sum  : {accumulate_base2(limit)}")
    print(f"Largest entry   : {entries[-1]}")
    print(f"Even entries    : {even_entries}")
    return entries

base2_report(8)
