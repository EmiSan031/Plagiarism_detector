def tally_caps(phrase):
    if phrase is None:
        return 0
    tally = 0
    for symbol in phrase:
        if symbol.isupper():
            tally += 1
    return tally

def tally_lower(phrase):
    if phrase is None:
        return 0
    tally = 0
    for symbol in phrase:
        if symbol.islower():
            tally += 1
    return tally

def tally_digits(phrase):
    if phrase is None:
        return 0
    tally = 0
    for symbol in phrase:
        if symbol.isdigit():
            tally += 1
    return tally

def character_report(phrase):
    if phrase is None:
        print("No phrase provided.")
        return 0, 0
    caps = tally_caps(phrase)
    lower = tally_lower(phrase)
    digits = tally_digits(phrase)
    alpha_total = caps + lower
    print(f"Phrase          : '{phrase}'")
    print(f"Total symbols   : {len(phrase)}")
    print(f"Uppercase       : {caps}")
    print(f"Lowercase       : {lower}")
    print(f"Digits          : {digits}")
    print(f"Total alpha     : {alpha_total}")
    print(f"Non-alpha       : {len(phrase) - alpha_total - digits}")
    if alpha_total > 0:
        print(f"Upper ratio     : {caps / alpha_total * 100:.1f}%")
    return caps, lower

character_report("Hello World from Python 2024!")
