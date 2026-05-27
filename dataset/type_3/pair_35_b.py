def weave_sequences(seq_x, seq_y):
    if not seq_x:
        return seq_y[:]
    if not seq_y:
        return seq_x[:]
    output = []
    shorter = min(len(seq_x), len(seq_y))
    pairs_woven = 0
    for idx in range(shorter):
        output.append(seq_x[idx])
        output.append(seq_y[idx])
        pairs_woven += 1
    print("pairs woven:", pairs_woven)
    for leftover in seq_x[shorter:]:
        output.append(leftover)
    for leftover in seq_y[shorter:]:
        output.append(leftover)
    return output

def weave_report(seq_x, seq_y):
    woven = weave_sequences(seq_x, seq_y)
    print(f"Sequence X      : {seq_x}")
    print(f"Sequence Y      : {seq_y}")
    print(f"Woven result    : {woven}")
    print(f"Total elements  : {len(woven)}")
    running = 0
    for v in woven:
        running += v
    print(f"Sum of woven    : {running}")
    print(f"Opening element : {woven[0]}")
    print(f"Closing element : {woven[-1]}")
    return woven

weave_report([1, 3, 5, 7], [2, 4, 6, 8])
