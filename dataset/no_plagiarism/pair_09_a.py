def compound_interest(principal, rate, years):
    balance = principal
    for _ in range(years):
        balance *= 1 + rate
    return round(balance, 2)

print(compound_interest(1000, 0.05, 3))
