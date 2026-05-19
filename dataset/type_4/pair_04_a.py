def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned == reverse_text(cleaned)

def reverse_words(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result = word + " " + result
    return result.strip()

def reverse_each_word(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result += reverse_text(word) + " "
    return result.strip()

print(reverse_text("python"))
print(is_palindrome("racecar"))
print(reverse_words("hello world foo"))
print(reverse_each_word("hello world"))
