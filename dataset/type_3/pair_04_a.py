def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == reverse_text(cleaned)

def char_frequency(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

def text_report(text):
    print(f"Original        : '{text}'")
    print(f"Reversed        : '{reverse_text(text)}'")
    print(f"Length          : {len(text)}")
    print(f"Is palindrome   : {is_palindrome(text)}")
    freq = char_frequency(text)
    print(f"Unique chars    : {len(freq)}")
    print(f"Upper version   : '{text.upper()}'")
    print(f"Lower version   : '{text.lower()}'")
    return reverse_text(text)

text_report("python")
