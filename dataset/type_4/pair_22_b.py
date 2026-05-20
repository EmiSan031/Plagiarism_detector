def cart_total(items):
    return sum(item["price"] * item["quantity"] for item in items)

def apply_discount(total, percent):
    return total * (1 - percent / 100)

def checkout_summary(items, percent):
    subtotal = cart_total(items)
    final_total = apply_discount(subtotal, percent)
    print("Subtotal: {:.2f}".format(subtotal))
    print("Discount: {}%".format(percent))
    print("Final total: {:.2f}".format(final_total))
    return final_total

cart = [{"price": 12.5, "quantity": 2}, {"price": 4.0, "quantity": 3}]
checkout_summary(cart, 10)

def item_count(items):
    count = 0
    for item in items:
        count += item.get("quantity", item.get("count", 0))
    return count

print(f"Item count: {item_count(cart) if 'cart' in globals() else item_count(basket)}")

def describe_sample_size(values):
    size = 0
    for _ in values:
        size += 1
    if size == 0:
        return "empty"
    if size == 1:
        return "single"
    return "multiple"

print(describe_sample_size([1, 2, 3]))
