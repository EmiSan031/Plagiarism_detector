def reads_same(phrase):
    normalized = phrase.lower().replace(" ", "")
    return normalized == normalized[::-1]


print(reads_same("oso"))
