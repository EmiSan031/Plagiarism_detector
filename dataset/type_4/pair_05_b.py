def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


print(count_vowels("Deteccion de plagio"))
