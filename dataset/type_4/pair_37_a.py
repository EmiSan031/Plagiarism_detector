def is_anagram(a, b):
    if len(a) != len(b):
        return False
    char_count = {}
    for char in a.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    for char in b.lower():
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True

def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if is_anagram(word, candidate):
            result.append(candidate)
    return result

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(find_anagrams("eat", ["tea", "tan", "ate", "bat"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "bat", "tab"]))
