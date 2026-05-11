def product_until(limit):
    if limit < 0:
        return None
    answer = 1
    current_values = range(2, limit + 1)
    for factor in current_values:
        answer *= factor
    return answer


print(product_until(6))
