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


print(count_letters("Deteccion de plagio"))
