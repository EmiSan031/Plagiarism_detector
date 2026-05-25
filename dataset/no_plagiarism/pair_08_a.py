def unique_words(text):
    words = text.lower().split()
    return sorted(set(words))

print(unique_words("data science data mining"))
