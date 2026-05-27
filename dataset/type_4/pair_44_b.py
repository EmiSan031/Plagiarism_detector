def to_ascii_codes(text):
    return list(text.encode('ascii'))

def from_ascii_codes(codes):
    return bytes(codes).decode('ascii')

def xor_encrypt(text, key):
    return "".join(chr(ord(c) ^ key) for c in text)

def xor_decrypt(text, key):
    return xor_encrypt(text, key)

def char_frequencies(text):
    from collections import Counter
    return dict(Counter(text))

msg = "Hello"
codes = to_ascii_codes(msg)
print(codes)
print(from_ascii_codes(codes))
encrypted = xor_encrypt(msg, 42)
print(xor_decrypt(encrypted, 42))
print(char_frequencies("mississippi"))
