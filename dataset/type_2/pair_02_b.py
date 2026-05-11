def product_until(limit):
    answer = 1
    for factor in range(2, limit + 1):
        answer *= factor
    return answer


print(product_until(5))
