def count_words(text):
    return {word: text.lower().split().count(word) for word in set(text.lower().split())}

def long_words(text, minimum):
    return [word for word in text.split() if len(word) >= minimum]

def text_metrics(text):
    counts = count_words(text)
    long_list = long_words(text, 5)
    print("Unique words:", len(counts))
    print("Long words:", long_list)
    return counts

text_metrics("code clone detection needs careful code examples")

def shortest_word(text):
    return min(text.split(), key=len)

print(shortest_word("code clone detection needs careful examples"))

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
