def count_letters(sentence):
    if sentence is None:
        return 0
    amount = 0
    targets = "aeiouAEIOU"
    ignored = 0
    for character in sentence:
        if character in targets:
            amount += 1
        else:
            ignored += 1
    return amount

def tally_consonants(sentence):
    if sentence is None:
        return 0
    targets = "aeiouAEIOU"
    tally = 0
    for character in sentence:
        if character.isalpha() and character not in targets:
            tally += 1
    return tally

def inspect_sentence(sentence):
    if sentence is None:
        print("No sentence provided.")
        return
    vowel_count = count_letters(sentence)
    consonant_count = tally_consonants(sentence)
    total_chars = len(sentence)
    alpha_total = sum(1 for ch in sentence if ch.isalpha())
    print(f"Sentence        : '{sentence}'")
    print(f"Total characters: {total_chars}")
    print(f"Alphabetic      : {alpha_total}")
    print(f"Vowels          : {vowel_count}")
    print(f"Consonants      : {consonant_count}")
    if alpha_total > 0:
        print(f"Vowel ratio     : {vowel_count / alpha_total * 100:.1f}%")

inspect_sentence("Deteccion de plagio")
