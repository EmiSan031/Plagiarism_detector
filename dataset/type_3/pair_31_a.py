def count_words(text):
    words = text.split()
    return len(words)

def word_stats(text):
    words = text.split()
    total = len(words)
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return total, longest, shortest

def text_report(text):
    total, longest, shortest = word_stats(text)
    print(f"Text            : '{text}'")
    print(f"Word count      : {total}")
    print(f"Longest word    : '{longest}'")
    print(f"Shortest word   : '{shortest}'")
    print(f"Character count : {len(text)}")
    print(f"Unique words    : {len(set(text.split()))}")
    return total

text_report("the quick brown fox jumps over the lazy dog")
