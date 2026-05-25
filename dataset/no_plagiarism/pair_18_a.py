def flatten_once(groups):
    result = []
    for group in groups:
        for item in group:
            result.append(item)
    return result

print(flatten_once([[1, 2], [3], [4, 5]]))
