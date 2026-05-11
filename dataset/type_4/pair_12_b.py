def word_frequency(words):
    return {word: words.count(word) for word in set(words)}


print(word_frequency(["a", "b", "a", "c", "b", "a"]))
