def calculate_cart_total(prices: list[float], tax_rate: float) -> float:
    subtotal = 0.0

    for price in prices:
        subtotal += price

    tax = subtotal * tax_rate
    total = subtotal + tax

    if total > 100:
        total = total - 10

    return round(total, 2)


if __name__ == "__main__":
    items = [24.50, 18.75, 66.20]
    print(calculate_cart_total(items, 0.08))
