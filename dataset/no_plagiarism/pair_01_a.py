def count_vowels(text):
    total = 0
    for char in text.lower():
        if char in "aeiou":
            total += 1
    return total

print(count_vowels("programming"))
