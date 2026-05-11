def flip_string(message):
    output = ""
    for symbol in message:
        output = symbol + output
    return output


print(flip_string("clone"))
