def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())

def remove_spaces(text):
    return text.replace(" ", "")

def repeat_string(text, times):
    return text * times

def count_words(sentence):
    return len(sentence.split())

def truncate(text, max_len):
    return text[:max_len] + "..." if len(text) > max_len else text

def pad_left(text, width, char=" "):
    return text.rjust(width, char)

def pad_right(text, width, char=" "):
    return text.ljust(width, char)

print(capitalize_words("hello world from python"))
print(remove_spaces("hello world"))
print(repeat_string("ab", 4))
print(count_words("the quick brown fox"))
print(truncate("hello world", 7))
print(pad_left("42", 6, "0"))
print(pad_right("hi", 6, "-"))
