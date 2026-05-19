def is_palindrome(text):
    # Ignore case and spaces.
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_palindromes(words):
    count = 0
    for word in words:
        if is_palindrome(word):
            count += 1
    return count

def get_palindromes(words):
    result = []
    for word in words:
        if is_palindrome(word):
            result.append(word)
    return result

def longest_palindrome(words):
    best = ""
    for word in words:
        if is_palindrome(word) and len(word) > len(best):
            best = word
    return best

candidates = ["racecar", "hello", "level", "world", "madam", "python", "civic"]
print(is_palindrome("anita lava la tina"))
print(count_palindromes(candidates))
print(get_palindromes(candidates))
print(longest_palindrome(candidates))
