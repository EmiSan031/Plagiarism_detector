from collections import Counter

def is_anagram(a, b):
    return Counter(a.lower()) == Counter(b.lower())

def find_anagrams(word, candidates):
    return [c for c in candidates if is_anagram(word, c)]

def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(find_anagrams("eat", ["tea", "tan", "ate", "bat"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "bat", "tab"]))
