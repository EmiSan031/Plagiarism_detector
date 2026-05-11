def largest_element(values):
    biggest = values[0]
    for current in values:
        if current > biggest:
            biggest = current
    return biggest


print(largest_element([10, 3, 22, 5, 11]))
