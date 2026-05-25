def format_phone(number):
    digits = "".join(char for char in number if char.isdigit())
    if len(digits) != 10:
        return digits
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

print(format_phone("5551234567"))
