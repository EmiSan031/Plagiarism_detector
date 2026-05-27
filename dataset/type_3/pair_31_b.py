def tally_tokens(sentence):
    if sentence.strip() == "":
        return 0
    tokens = sentence.split()
    return len(tokens)

def token_stats(sentence):
    if sentence.strip() == "":
        return 0, "", "", 0
    tokens = sentence.split()
    qty = len(tokens)
    biggest = ""
    for token in tokens:
        if len(token) > len(biggest):
            biggest = token
    smallest = tokens[0]
    for token in tokens:
        if len(token) < len(smallest):
            smallest = token
    short_count = 0
    for token in tokens:
        if len(token) <= 3:
            short_count += 1
    return qty, biggest, smallest, short_count

def sentence_report(sentence):
    qty, biggest, smallest, short_count = token_stats(sentence)
    print(f"Sentence        : '{sentence}'")
    print(f"Token count     : {qty}")
    print(f"Longest token   : '{biggest}'")
    print(f"Shortest token  : '{smallest}'")
    print(f"Short words(<=3): {short_count}")
    print(f"Char count      : {len(sentence)}")
    print(f"Distinct tokens : {len(set(sentence.split()))}")
    return qty

sentence_report("the quick brown fox jumps over the lazy dog")
