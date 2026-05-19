def remove_duplicates(values):
    return list(dict.fromkeys(values))

def has_duplicates(values):
    return len(values) != len(set(values))

def count_unique(values):
    return len(set(values))

def get_duplicates(values):
    seen = set()
    return list({v for v in values if v in seen or seen.add(v)})

data = [1, 2, 1, 3, 2, 4, 5, 4]
print(remove_duplicates(data))
print(has_duplicates(data))
print(count_unique(data))
print(get_duplicates(data))
