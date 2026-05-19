def count_items(tokens):
    table = {}
    for token in tokens:
        if token not in table:
            table[token] = 0
        table[token] += 1
    return table

def dominant_token(tokens):
    table = count_items(tokens)
    leading = None
    peak = 0
    for token in table:
        if table[token] > peak:
            peak = table[token]
            leading = token
    return leading, peak

def token_report(tokens):
    print(f"Token list      : {tokens}")
    print(f"Total tokens    : {len(tokens)}")
    table = count_items(tokens)
    print(f"Distinct tokens : {len(table)}")
    print(f"Token counts:")
    for token in table:
        bar = "*" * table[token]
        print(f"  '{token}': {table[token]}  {bar}")
    leading, peak = dominant_token(tokens)
    print(f"Most common     : '{leading}' ({peak} times)")

token_report(["red", "blue", "red", "green", "blue", "red"])
