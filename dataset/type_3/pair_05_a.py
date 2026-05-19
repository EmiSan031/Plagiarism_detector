def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonants += 1
    return consonants

def analyze_text(text):
    total_vowels = count_vowels(text)
    total_consonants = count_consonants(text)
    total_chars = len(text)
    total_letters = sum(1 for c in text if c.isalpha())
    print(f"Text            : '{text}'")
    print(f"Total characters: {total_chars}")
    print(f"Letters         : {total_letters}")
    print(f"Vowels          : {total_vowels}")
    print(f"Consonants      : {total_consonants}")
    if total_letters > 0:
        print(f"Vowel ratio     : {total_vowels / total_letters * 100:.1f}%")

analyze_text("Deteccion de plagio")
