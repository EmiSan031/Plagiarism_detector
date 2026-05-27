def to_ascii_codes(text):
    codes = []
    for char in text:
        codes.append(ord(char))
    return codes

def from_ascii_codes(codes):
    result = ""
    for code in codes:
        result += chr(code)
    return result

def xor_encrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

def xor_decrypt(text, key):
    return xor_encrypt(text, key)

def char_frequencies(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

msg = "Hello"
codes = to_ascii_codes(msg)
print(codes)
print(from_ascii_codes(codes))
encrypted = xor_encrypt(msg, 42)
print(xor_decrypt(encrypted, 42))
print(char_frequencies("mississippi"))
