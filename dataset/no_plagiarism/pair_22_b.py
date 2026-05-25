def acronym(phrase):
    letters = []
    for word in phrase.split():
        if word:
            letters.append(word[0].upper())
    return "".join(letters)

print(acronym("object oriented programming"))
