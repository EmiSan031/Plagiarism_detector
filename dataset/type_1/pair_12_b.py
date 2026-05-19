def word_frequency(words):
    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts
def most_frequent(words):
    counts = word_frequency(words)
    best = None
    best_count = 0
    for word in counts:
        if counts[word] > best_count:
            best = word
            best_count = counts[word]
    return best
# Return the word that appears the fewest times.
def least_frequent(words):
    counts = word_frequency(words)
    worst = None
    worst_count = None
    for word in counts:
        if worst_count is None or counts[word] < worst_count:
            worst = word
            worst_count = counts[word]
    return worst
def unique_words(words):
    return list(word_frequency(words).keys())

# Count repeated strings.
sample = ["a", "b", "a", "c", "b", "a", "c", "c", "c"]
print(word_frequency(sample))
print(most_frequent(sample))
print(least_frequent(sample))
print(unique_words(sample))
