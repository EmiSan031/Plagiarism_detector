def lists_to_dict(keys, values):
    return dict(zip(keys, values))

def invert_dict(mapping):
    return {v: k for k, v in mapping.items()}

def merge_dicts(a, b):
    return {**a, **b}

def dict_max_value(mapping):
    return max(mapping, key=mapping.get)

names = ["alice", "bob", "carol"]
scores = [90, 85, 92]
print(lists_to_dict(names, scores))
print(invert_dict({"a": 1, "b": 2, "c": 3}))
print(merge_dicts({"x": 1}, {"y": 2, "x": 99}))
print(dict_max_value(lists_to_dict(names, scores)))
