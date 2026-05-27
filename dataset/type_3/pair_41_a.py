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

def cipher_report(text, shift):
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Original        : '{text}'")
    print(f"Shift           : {shift}")
    print(f"Encrypted       : '{encrypted}'")
    print(f"Decrypted       : '{decrypted}'")
    print(f"Matches original: {decrypted == text}")
    print(f"Text length     : {len(text)}")
    print(f"Alpha chars     : {sum(1 for c in text if c.isalpha())}")
    return encrypted

cipher_report("Hello World", 3)
