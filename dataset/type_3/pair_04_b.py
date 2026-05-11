def flip_string(message):
    if message == "":
        return ""
    output = ""
    for symbol in message:
        output = symbol + output
    output = output.strip()
    return output


print(flip_string("python"))
