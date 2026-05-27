def partition(data, block_size):
    if block_size <= 0:
        return [data[:]]
    blocks = []
    for start in range(0, len(data), block_size):
        blocks.append(data[start:start + block_size])
    return blocks

def invert_blocks(data, block_size):
    if block_size <= 0:
        return data[:]
    blocks = partition(data, block_size)
    output = []
    for block in blocks:
        flipped = block[::-1]
        for entry in flipped:
            output.append(entry)
    return output

def block_sums(data, block_size):
    blocks = partition(data, block_size)
    sums = []
    for block in blocks:
        block_total = 0
        for entry in block:
            block_total += entry
        sums.append(block_total)
    return sums

def block_report(data, block_size):
    if block_size <= 0:
        print(f"Invalid block size: {block_size}")
        return data[:]
    blocks = partition(data, block_size)
    inverted = invert_blocks(data, block_size)
    sums = block_sums(data, block_size)
    print(f"Original data   : {data}")
    print(f"Block size      : {block_size}")
    print(f"Blocks          : {blocks}")
    print(f"Block count     : {len(blocks)}")
    print(f"Block sums      : {sums}")
    print(f"Inverted blocks : {inverted}")
    print(f"Total elements  : {len(inverted)}")
    return inverted

block_report([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
