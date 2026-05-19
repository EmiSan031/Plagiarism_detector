def word_frequency(words):
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts

def most_frequent(words):
    counts = word_frequency(words)
    top_word = None
    top_count = 0
    for word in counts:
        if counts[word] > top_count:
            top_count = counts[word]
            top_word = word
    return top_word, top_count

def frequency_report(words):
    print(f"Word list       : {words}")
    print(f"Total words     : {len(words)}")
    counts = word_frequency(words)
    print(f"Unique words    : {len(counts)}")
    print(f"Frequencies:")
    for word in counts:
        bar = "*" * counts[word]
        print(f"  '{word}': {counts[word]}  {bar}")
    top_word, top_count = most_frequent(words)
    print(f"Most frequent   : '{top_word}' ({top_count} times)")

frequency_report(["a", "b", "a", "c", "b", "a"])
