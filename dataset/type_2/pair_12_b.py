def count_items(tokens):
    table = {}
    for token in tokens:
        if token not in table:
            table[token] = 0
        table[token] += 1
    return table


print(count_items(["red", "blue", "red", "green", "blue", "red"]))
