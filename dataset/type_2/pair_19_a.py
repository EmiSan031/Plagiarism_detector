def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def remove_special_chars(text):
    result = ""
    for char in text:
        if char.isalpha() or char == " ":
            result += char
    return result

def palindrome_report(text):
    cleaned = text.lower().replace(" ", "")
    sanitized = remove_special_chars(text).lower().replace(" ", "")
    original_check = is_palindrome(text)
    print(f"Original text   : '{text}'")
    print(f"Cleaned version : '{cleaned}'")
    print(f"Length (cleaned): {len(cleaned)}")
    print(f"Is palindrome   : {original_check}")
    if original_check:
        print(f"  -> '{text}' reads the same forwards and backwards!")
    else:
        print(f"  -> '{text}' does NOT read the same both ways.")
    print(f"First character : '{cleaned[0] if cleaned else 'N/A'}'")
    print(f"Last character  : '{cleaned[-1] if cleaned else 'N/A'}'")

test_phrases = ["anita lava la tina", "hello", "racecar", "python"]
for phrase in test_phrases:
    palindrome_report(phrase)
    print()
