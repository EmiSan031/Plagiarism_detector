def tax_bracket(income):
    if income < 10000:
        return "low"
    if income < 50000:
        return "middle"
    return "high"

print(tax_bracket(42000))
