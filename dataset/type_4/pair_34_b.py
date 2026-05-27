def caesar_encrypt(text, shift):
    def shift_char(char, base, shift):
        return chr((ord(char) - base + shift) % 26 + base)
    upper = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "".join(shift_char(c, ord('A'), shift) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    )
    lower = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "".join(shift_char(c, ord('a'), shift) for c in "abcdefghijklmnopqrstuvwxyz")
    )
    return text.translate(upper).translate(lower)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_caesar(text):
    return [(shift, caesar_decrypt(text, shift)) for shift in range(1, 26)]

print(caesar_encrypt("Hello, World!", 3))
print(caesar_decrypt("Khoor, Zruog!", 3))
print(brute_force_caesar("Khoor")[0])
