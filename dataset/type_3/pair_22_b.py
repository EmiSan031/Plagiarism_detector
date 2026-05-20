def cart_total(items):
    total = 0
    for item in items:
        if item["quantity"] > 0:
            total += item["price"] * item["quantity"]
    return total

def apply_discount(total, percent):
    if percent < 0:
        percent = 0
    discount = total * percent / 100
    return total - discount

def add_tax(total, percent):
    return total + total * percent / 100

def checkout_summary(items, percent):
    subtotal = cart_total(items)
    discounted = apply_discount(subtotal, percent)
    final_total = add_tax(discounted, 8)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {percent}%")
    print(f"With tax: {final_total:.2f}")
    return final_total

cart = [{"price": 12.5, "quantity": 2}, {"price": 4.0, "quantity": 3}]
checkout_summary(cart, 10)

def item_count(items):
    count = 0
    for item in items:
        count += item.get("quantity", item.get("count", 0))
    return count

print(f"Item count: {item_count(cart) if 'cart' in globals() else item_count(basket)}")
