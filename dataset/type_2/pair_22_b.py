def basket_amount(goods):
    amount = 0
    for good in goods:
        amount += good["cost"] * good["count"]
    return amount

def subtract_sale(amount, rate):
    reduction = amount * rate / 100
    return amount - reduction

def receipt_details(goods, rate):
    before = basket_amount(goods)
    after = subtract_sale(before, rate)
    print(f"Before sale: {before:.2f}")
    print(f"Sale rate: {rate}%")
    print(f"Amount due: {after:.2f}")
    return after

basket = [{"cost": 8.0, "count": 4}, {"cost": 3.5, "count": 2}]
receipt_details(basket, 15)

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
