def largest_element(values):
    if len(values) == 0:
        return None
    biggest = values[0]
    changes = 0
    for current in values:
        if current > biggest:
            biggest = current
            changes += 1
    return biggest


print(largest_element([4, 9, 2, 15, 6]))
