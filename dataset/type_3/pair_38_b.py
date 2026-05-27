def shift_left(sequence, moves):
    size = len(sequence)
    if size == 0:
        return []
    if moves < 0:
        moves = 0
    moves = moves % size
    return sequence[moves:] + sequence[:moves]

def shift_right(sequence, moves):
    size = len(sequence)
    if size == 0:
        return []
    if moves < 0:
        moves = 0
    moves = moves % size
    return sequence[size - moves:] + sequence[:size - moves]

def is_rotation(original, candidate):
    if len(original) != len(candidate):
        return False
    doubled = original + original
    return candidate in [doubled[i:i+len(original)] for i in range(len(original))]

def shift_report(sequence, moves):
    shifted_l = shift_left(sequence, moves)
    shifted_r = shift_right(sequence, moves)
    print(f"Original        : {sequence}")
    print(f"Moves           : {moves}")
    print(f"Shifted left    : {shifted_l}")
    print(f"Shifted right   : {shifted_r}")
    print(f"Size            : {len(sequence)}")
    print(f"Is rotation (L) : {is_rotation(sequence, shifted_l)}")
    print(f"Opening (left)  : {shifted_l[0]}")
    print(f"Closing (left)  : {shifted_l[-1]}")
    return shifted_l

shift_report([1, 2, 3, 4, 5, 6], 2)
