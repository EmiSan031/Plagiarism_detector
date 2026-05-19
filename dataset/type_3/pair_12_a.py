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

def unique_words(words):
    seen = []
    for word in words:
        if word not in seen:
            seen.append(word)
    return seen

def words_appearing_once(words):
    counts = word_frequency(words)
    result = []
    for word in counts:
        if counts[word] == 1:
            result.append(word)
    return result

sample = ["a", "b", "a", "c", "b", "a", "d"]
print(word_frequency(sample))
print(most_frequent(sample))
print(unique_words(sample))
print(words_appearing_once(sample))
