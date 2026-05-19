def word_frequency(words):
    return {word: words.count(word) for word in set(words)}

def most_frequent(words):
    freq = word_frequency(words)
    return max(freq, key=freq.get)

def unique_words(words):
    return list(dict.fromkeys(words))

def words_appearing_once(words):
    freq = word_frequency(words)
    return [word for word, count in freq.items() if count == 1]

sample = ["a", "b", "a", "c", "b", "a", "d"]
print(word_frequency(sample))
print(most_frequent(sample))
print(unique_words(sample))
print(words_appearing_once(sample))
