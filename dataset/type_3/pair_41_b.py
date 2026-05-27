def encode_message(message, offset):
    if offset < 0:
        offset = offset % 26
    output = ""
    skipped = 0
    for symbol in message:
        if symbol.isalpha():
            anchor = ord('A') if symbol.isupper() else ord('a')
            output += chr((ord(symbol) - anchor + offset) % 26 + anchor)
        else:
            output += symbol
            skipped += 1
    print("non-alpha skipped:", skipped)
    return output

def decode_message(message, offset):
    return encode_message(message, -offset)

def encoding_report(message, offset):
    encoded = encode_message(message, offset)
    decoded = decode_message(encoded, offset)
    print(f"Original        : '{message}'")
    print(f"Offset          : {offset}")
    print(f"Encoded         : '{encoded}'")
    print(f"Decoded         : '{decoded}'")
    print(f"Matches original: {decoded == message}")
    print(f"Message length  : {len(message)}")
    print(f"Alpha chars     : {sum(1 for s in message if s.isalpha())}")
    return encoded

encoding_report("Hello World", 3)
