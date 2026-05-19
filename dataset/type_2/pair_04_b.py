def flip_string(message):
    output = ""
    for symbol in message:
        output = symbol + output
    return output

def check_palindrome(message):
    normalized = message.lower().replace(" ", "")
    return normalized == flip_string(normalized)

def inspect_message(message):
    print(f"Input message   : '{message}'")
    print(f"Flipped message : '{flip_string(message)}'")
    print(f"Character count : {len(message)} symbols")
    palindrome_result = check_palindrome(message)
    if palindrome_result:
        print(f"Palindrome      : Yes")
    else:
        print(f"Palindrome      : No")
    print(f"All caps        : '{message.upper()}'")
    print(f"All lower       : '{message.lower()}'")

entries = ["clone", "madam", "world", "civic"]
for entry in entries:
    inspect_message(entry)
    print()
