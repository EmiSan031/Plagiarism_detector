def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def remove_punctuation(text):
    punctuation = set("!.,;:?-()[]{}")
    result = ""
    for char in text:
        if char not in punctuation:
            result += char
    return result

def normalize_spaces(text):
    result = ""
    prev_space = False
    for char in text:
        if char == " ":
            if not prev_space:
                result += char
            prev_space = True
        else:
            result += char
            prev_space = False
    return result.strip()

def keep_only_alpha(text):
    result = ""
    for char in text:
        if char.isalpha() or char == " ":
            result += char
    return result

print(remove_vowels("Hello World"))
print(remove_punctuation("Hello, World! How are you?"))
print(normalize_spaces("too   many    spaces"))
print(keep_only_alpha("Hello, W0rld! 123"))
