def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for char in text:
        if char in vowels:
            count += 1

    return count


# Demo input.
print(count_vowels("Deteccion de plagio"))
