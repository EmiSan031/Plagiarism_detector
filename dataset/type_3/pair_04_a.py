def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


print(reverse_text("python"))
