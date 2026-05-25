def title_case(text):
    words = []
    for word in text.split():
        words.append(word[:1].upper() + word[1:].lower())
    return " ".join(words)

print(title_case("hello WORLD"))
