def capitalize_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        capitalized = word[0].upper() + word[1:].lower()
        result.append(capitalized)
    return " ".join(result)

def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result

def repeat_string(text, times):
    result = ""
    for _ in range(times):
        result += text
    return result

def count_words(sentence):
    words = sentence.split()
    count = 0
    for _ in words:
        count += 1
    return count

print(capitalize_words("hello world from python"))
print(remove_spaces("hello world"))
print(repeat_string("ab", 4))
print(count_words("the quick brown fox"))
