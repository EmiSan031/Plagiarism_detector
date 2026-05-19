def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
def count_consonants(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
def count_spaces(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count
# Count numeric characters in text.
def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count
def char_summary(text):
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Spaces:", count_spaces(text))
    print("Digits:", count_digits(text))
# Demo input.
sample = "Deteccion de plagio 2024"
char_summary(sample)
