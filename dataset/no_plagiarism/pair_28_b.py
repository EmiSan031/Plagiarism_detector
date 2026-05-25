def filter_prefix(words, prefix):
    result = []
    for word in words:
        if word.startswith(prefix):
            result.append(word)
    return result

print(filter_prefix(["car", "cat", "dog"], "ca"))
