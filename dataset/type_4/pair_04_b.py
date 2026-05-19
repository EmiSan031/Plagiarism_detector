def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalpha())
    return cleaned == cleaned[::-1]

def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))

def reverse_each_word(sentence):
    return " ".join(w[::-1] for w in sentence.split())

def remove_spaces(text):
    return "".join(text.split())

def count_char(text, char):
    return text.count(char)

def title_case(text):
    return " ".join(w.capitalize() for w in text.split())

def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(reverse_text("python"))
print(is_palindrome("racecar"))
print(reverse_words("hello world foo"))
print(reverse_each_word("hello world"))
print(remove_spaces("hola mundo"))
print(count_char("mississippi", "s"))
print(title_case("hello world"))
print(is_anagram("listen", "silent"))
