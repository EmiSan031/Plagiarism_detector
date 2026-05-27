import re

def remove_vowels(text):
    return re.sub(r"[aeiouAEIOU]", "", text)

def remove_punctuation(text):
    return re.sub(r"[^\w\s]", "", text)

def normalize_spaces(text):
    return re.sub(r" +", " ", text).strip()

def keep_only_alpha(text):
    return re.sub(r"[^a-zA-Z ]", "", text)

print(remove_vowels("Hello World"))
print(remove_punctuation("Hello, World! How are you?"))
print(normalize_spaces("too   many    spaces"))
print(keep_only_alpha("Hello, W0rld! 123"))
