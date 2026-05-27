def split_chunks(values, size):
    chunks = []
    for i in range(0, len(values), size):
        chunks.append(values[i:i + size])
    return chunks

def reverse_chunks(values, size):
    chunks = split_chunks(values, size)
    result = []
    for chunk in chunks:
        reversed_chunk = chunk[::-1]
        for item in reversed_chunk:
            result.append(item)
    return result

def chunk_report(values, size):
    chunks = split_chunks(values, size)
    reversed_list = reverse_chunks(values, size)
    print(f"Original list   : {values}")
    print(f"Chunk size      : {size}")
    print(f"Chunks          : {chunks}")
    print(f"Number of chunks: {len(chunks)}")
    print(f"Reversed chunks : {reversed_list}")
    print(f"Total elements  : {len(reversed_list)}")
    return reversed_list

chunk_report([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
