def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == reverse_text(cleaned)

def analyze_text(text):
    print(f"Original text   : '{text}'")
    print(f"Reversed text   : '{reverse_text(text)}'")
    print(f"Length          : {len(text)} characters")
    palindrome_check = is_palindrome(text)
    if palindrome_check:
        print(f"Palindrome      : Yes")
    else:
        print(f"Palindrome      : No")
    print(f"Uppercase       : '{text.upper()}'")
    print(f"Lowercase       : '{text.lower()}'")

words = ["python", "racecar", "hello", "level"]
for word in words:
    analyze_text(word)
    print()
