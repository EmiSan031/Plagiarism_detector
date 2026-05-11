def word_frequency(words):
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts


print(word_frequency(["a", "b", "a", "c", "b", "a"]))
