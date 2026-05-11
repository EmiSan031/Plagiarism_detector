def count_items(tokens):
    table = {}
    total = 0
    for token in tokens:
        if token == "":
            continue
        if token not in table:
            table[token] = 0
        table[token] += 1
        total += 1
    print("total:", total)
    return table


print(count_items(["a", "b", "a", "c", "b", "a"]))
