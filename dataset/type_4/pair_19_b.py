def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("anita lava la tina"))
