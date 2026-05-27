import itertools

def interleave(a, b):
    pairs = list(itertools.chain.from_iterable(zip(a, b)))
    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)
    return pairs + list(longer[len(shorter):])

def split_in_half(items):
    mid = len(items) // 2
    return items[:mid], items[mid:]

def chunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]

def flatten(nested):
    return list(itertools.chain.from_iterable(nested))

def sliding_window(items, size):
    return [items[i:i + size] for i in range(len(items) - size + 1)]

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(interleave([1, 3, 5], [2, 4, 6]))
print(split_in_half(data))
print(chunk(data, 3))
print(flatten([[1, 2], [3, 4], [5]]))
print(sliding_window(data, 3))
