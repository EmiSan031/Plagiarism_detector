# Separate positive and negative transaction totals.
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

def balance_report(transactions):
    income = deposits(transactions)
    spent = withdrawals(transactions)
    balance = income - spent
    print(f"Deposits: {income}")
    print(f"Withdrawals: {spent}")
    print(f"Balance: {balance}")
    return balance

balance_report([100, -25, 40, -10])

def transaction_count(transactions):
    count = 0
    for amount in transactions:
        if amount != 0:
            count += 1
    return count

print(f"Transactions: {transaction_count([100, -25, 40, -10])}")
