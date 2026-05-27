def compute_order_amount(values: list[float], fee_percent: float) -> float:
    base_amount = 0.0

    for value in values:
        base_amount += value

    fee = base_amount * fee_percent
    final_amount = base_amount + fee

    if final_amount > 120:
        final_amount = final_amount - 15

    return round(final_amount, 2)


if __name__ == "__main__":
    products = [32.40, 41.10, 55.80]
    print(compute_order_amount(products, 0.06))
