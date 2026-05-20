def tally_terms(sentence):
    terms = sentence.lower().split()
    totals = {}
    for term in terms:
        if term not in totals:
            totals[term] = 0
        totals[term] += 1
    return totals

def large_terms(sentence, size):
    selected = []
    for term in sentence.split():
        if len(term) >= size:
            selected.append(term)
    return selected

def sentence_metrics(sentence):
    totals = tally_terms(sentence)
    selected = large_terms(sentence, 6)
    print(f"Different terms: {len(totals)}")
    print(f"Large terms: {selected}")
    return totals

sentence_metrics("software metrics compare similar software fragments")

def shortest_word(text):
    words = text.split()
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

print(shortest_word("code clone detection needs careful examples"))
