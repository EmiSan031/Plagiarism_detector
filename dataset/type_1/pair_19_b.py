def is_palindrome(text):
    # Ignore case and spaces.
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


print(is_palindrome("anita lava la tina"))
