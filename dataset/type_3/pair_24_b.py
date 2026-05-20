def clean_word(word):
    return word.lower().strip(".,!?")

def count_words(text):
    words = text.split()
    counts = {}
    for word in words:
        clean = clean_word(word)
        if clean not in counts:
            counts[clean] = 0
        counts[clean] += 1
    return counts

def long_words(text, minimum):
    result = []
    for word in text.split():
        clean = clean_word(word)
        if len(clean) >= minimum:
            result.append(clean)
    return result

def text_metrics(text):
    counts = count_words(text)
    long_list = long_words(text, 5)
    print(f"Unique words: {len(counts)}")
    print(f"Long words: {long_list}")
    print(f"Total words: {len(text.split())}")
    return counts

text_metrics("Code clone detection needs careful code examples.")
