def deposits(transactions):
    return sum(amount for amount in transactions if amount > 0)

def withdrawals(transactions):
    return sum(-amount for amount in transactions if amount < 0)

def balance_report(transactions):
    totals = {
        "income": deposits(transactions),
        "spent": withdrawals(transactions),
    }
    balance = totals["income"] - totals["spent"]
    print("Deposits:", totals["income"])
    print("Withdrawals:", totals["spent"])
    print("Balance:", balance)
    return balance

balance_report([100, -25, 40, -10])

def transaction_count(transactions):
    count = 0
    for amount in transactions:
        if amount != 0:
            count += 1
    return count

print(f"Transactions: {transaction_count([100, -25, 40, -10])}")

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
