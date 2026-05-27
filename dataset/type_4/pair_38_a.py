def lists_to_dict(keys, values):
    result = {}
    for i in range(min(len(keys), len(values))):
        result[keys[i]] = values[i]
    return result

def invert_dict(mapping):
    result = {}
    for key in mapping:
        result[mapping[key]] = key
    return result

def merge_dicts(a, b):
    result = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        result[key] = b[key]
    return result

def dict_max_value(mapping):
    best_key = None
    best_val = None
    for key in mapping:
        if best_val is None or mapping[key] > best_val:
            best_key = key
            best_val = mapping[key]
    return best_key

names = ["alice", "bob", "carol"]
scores = [90, 85, 92]
print(lists_to_dict(names, scores))
print(invert_dict({"a": 1, "b": 2, "c": 3}))
print(merge_dicts({"x": 1}, {"y": 2, "x": 99}))
print(dict_max_value(lists_to_dict(names, scores)))
