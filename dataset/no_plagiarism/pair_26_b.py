def apply_bonus(salaries, percent):
    updated = {}
    for name, salary in salaries.items():
        updated[name] = salary * (1 + percent)
    return updated

print(apply_bonus({"Ana": 100, "Luis": 80}, 0.1))
