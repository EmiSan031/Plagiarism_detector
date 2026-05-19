def count_vowels(text):
    return sum(1 for c in text if c in set("aeiouAEIOU"))

def count_consonants(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for c in text if c.isalpha() and c not in vowels)

def count_digits(text):
    return sum(1 for c in text if c.isdigit())

def count_spaces(text):
    return text.count(" ")

def count_uppercase(text):
    return sum(1 for c in text if c.isupper())

def count_lowercase(text):
    return sum(1 for c in text if c.islower())

def char_summary(text):
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Digits:", count_digits(text))

sample = "Deteccion de plagio 2024"
char_summary(sample)
print(count_spaces(sample))
print(count_uppercase(sample))
print(count_lowercase(sample))
