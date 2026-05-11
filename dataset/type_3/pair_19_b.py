def reads_same(phrase):
    if phrase == "":
        return True
    normalized = phrase.lower().replace(" ", "")
    normalized = normalized.replace(",", "")
    result = normalized == normalized[::-1]
    return result


print(reads_same("anita lava la tina"))
