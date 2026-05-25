def cart_total(items):
    subtotal = sum(price for price, quantity in items for _ in range(quantity))
    shipping = 0 if subtotal > 50 else 5
    return subtotal + shipping

print(cart_total([(10, 2), (15, 1)]))
