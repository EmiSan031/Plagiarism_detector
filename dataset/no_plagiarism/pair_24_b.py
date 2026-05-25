def group_by_length(words):
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups

print(group_by_length(["ai", "code", "data"]))
