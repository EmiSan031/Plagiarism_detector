def count_letters(sentence):
    amount = 0
    targets = "aeiouAEIOU"
    for character in sentence:
        if character in targets:
            amount += 1
    return amount

def count_non_vowels(sentence):
    non_vowels = 0
    targets = "aeiouAEIOU"
    for character in sentence:
        if character.isalpha() and character not in targets:
            non_vowels += 1
    return non_vowels

def inspect_sentence(sentence):
    vowel_count = count_letters(sentence)
    consonant_count = count_non_vowels(sentence)
    alpha_total = sum(1 for ch in sentence if ch.isalpha())
    blank_count = sentence.count(" ")
    print(f"Sentence        : '{sentence}'")
    print(f"Vowels found    : {vowel_count}")
    print(f"Consonants found: {consonant_count}")
    print(f"Alphabetic chars: {alpha_total}")
    print(f"Spaces detected : {blank_count}")
    if alpha_total > 0:
        ratio = (vowel_count / alpha_total) * 100
        print(f"Vowel ratio     : {ratio:.1f}%")

inspect_sentence("Analisis de codigo")
