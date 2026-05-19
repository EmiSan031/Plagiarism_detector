def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned = cleaned + char.lower()
    reversed_cleaned = reverse_text(cleaned)
    return cleaned == reversed_cleaned

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ""
    for word in words:
        reversed_sentence = word + " " + reversed_sentence
    return reversed_sentence.strip()

def reverse_each_word(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result += reverse_text(word) + " "
    return result.strip()

print(reverse_text("python"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(reverse_words("hello world foo"))
print(reverse_each_word("hello world"))
