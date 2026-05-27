def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_caesar(text):
    results = []
    for shift in range(1, 26):
        results.append((shift, caesar_decrypt(text, shift)))
    return results

print(caesar_encrypt("Hello, World!", 3))
print(caesar_decrypt("Khoor, Zruog!", 3))
print(brute_force_caesar("Khoor")[0])
