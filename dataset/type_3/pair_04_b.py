def flip_string(message):
    if message == "":
        return ""
    output = ""
    for symbol in message:
        output = symbol + output
    output = output.strip()
    return output

def check_palindrome(message):
    normalized = message.lower().replace(" ", "")
    return normalized == flip_string(normalized)

def symbol_frequency(message):
    freq = {}
    for symbol in message:
        if symbol not in freq:
            freq[symbol] = 0
        freq[symbol] += 1
    return freq

def message_report(message):
    print(f"Original        : '{message}'")
    print(f"Flipped         : '{flip_string(message)}'")
    print(f"Length          : {len(message)}")
    print(f"Is palindrome   : {check_palindrome(message)}")
    freq = symbol_frequency(message)
    print(f"Distinct symbols: {len(freq)}")
    print(f"Upper form      : '{message.upper()}'")
    print(f"Lower form      : '{message.lower()}'")
    return flip_string(message)

message_report("python")
