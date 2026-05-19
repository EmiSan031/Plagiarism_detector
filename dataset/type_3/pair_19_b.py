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

def count_palindromes(words):
    total = 0
    for word in words:
        if is_palindrome(word):
            total += 1
    return total

def get_palindromes(words):
    found = []
    for word in words:
        if is_palindrome(word):
            found.append(word)
    return found

def longest_palindrome(words):
    champion = ""
    for word in words:
        if is_palindrome(word) and len(word) > len(champion):
            champion = word
    return champion

candidates = ["racecar", "hello", "level", "world", "madam", "civic"]
print(is_palindrome("anita lava la tina"))
print(count_palindromes(candidates))
print(get_palindromes(candidates))
print(longest_palindrome(candidates))
