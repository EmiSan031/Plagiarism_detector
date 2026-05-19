def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    consonants = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char.isalpha() and char not in vowels:
            consonants += 1
    return consonants

def analyze_text(text):
    total_vowels = count_vowels(text)
    total_consonants = count_consonants(text)
    total_letters = sum(1 for c in text if c.isalpha())
    total_spaces = text.count(" ")
    print(f"Text            : '{text}'")
    print(f"Total vowels    : {total_vowels}")
    print(f"Total consonants: {total_consonants}")
    print(f"Total letters   : {total_letters}")
    print(f"Total spaces    : {total_spaces}")
    if total_letters > 0:
        pct = (total_vowels / total_letters) * 100
        print(f"Vowel percentage: {pct:.1f}%")

analyze_text("Deteccion de plagio")
