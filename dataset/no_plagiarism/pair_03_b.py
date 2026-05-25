def word_lengths(sentence):
    lengths = {}
    for word in sentence.split():
        lengths[word] = len(word)
    return lengths

print(word_lengths("machine learning project"))
