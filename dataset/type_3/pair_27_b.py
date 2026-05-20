def deposits(transactions):
    total = 0
    for amount in transactions:
        if amount > 0:
            total += amount
    return total

def withdrawals(transactions):
    total = 0
    for amount in transactions:
        if amount < 0:
            total += abs(amount)
    return total

def largest_withdrawal(transactions):
    largest = 0
    for amount in transactions:
        if amount < 0 and abs(amount) > largest:
            largest = abs(amount)
    return largest

def balance_report(transactions):
    income = deposits(transactions)
    spent = withdrawals(transactions)
    balance = income - spent
    largest = largest_withdrawal(transactions)
    print(f"Deposits: {income}")
    print(f"Withdrawals: {spent}")
    print(f"Largest withdrawal: {largest}")
    print(f"Balance: {balance}")
    return balance

balance_report([100, -25, 40, -10])
