def count_uppercase(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count

def count_lowercase(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    return count

def case_report(text):
    upper = count_uppercase(text)
    lower = count_lowercase(text)
    total_alpha = upper + lower
    print(f"Text            : '{text}'")
    print(f"Total chars     : {len(text)}")
    print(f"Uppercase       : {upper}")
    print(f"Lowercase       : {lower}")
    print(f"Total alpha     : {total_alpha}")
    print(f"Non-alpha       : {len(text) - total_alpha}")
    if total_alpha > 0:
        print(f"Upper ratio     : {upper / total_alpha * 100:.1f}%")
    return upper, lower

case_report("Hello World from Python 2024!")
