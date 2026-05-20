def count_words(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts

def long_words(text, minimum):
    result = []
    for word in text.split():
        if len(word) >= minimum:
            result.append(word)
    return result

def text_metrics(text):
    counts = count_words(text)
    long_list = long_words(text, 5)
    print(f"Unique words: {len(counts)}")
    print(f"Long words: {long_list}")
    return counts

text_metrics("code clone detection needs careful code examples")

def shortest_word(text):
    words = text.split()
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

print(shortest_word("code clone detection needs careful examples"))
