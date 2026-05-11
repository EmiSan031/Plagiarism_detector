def count_letters(sentence):
    amount = 0
    targets = "aeiouAEIOU"
    for character in sentence:
        if character in targets:
            amount += 1
    return amount


print(count_letters("Analisis de codigo"))
