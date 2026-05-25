def shopping_discount(total, member):
    if total >= 100 and member:
        return total * 0.8
    if total >= 100:
        return total * 0.9
    return total

print(shopping_discount(120, True))
