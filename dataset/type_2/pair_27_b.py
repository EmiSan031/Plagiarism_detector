def credits(entries):
    amount = 0
    for entry in entries:
        if entry > 0:
            amount += entry
    return amount

def debits(entries):
    amount = 0
    for entry in entries:
        if entry < 0:
            amount += abs(entry)
    return amount

def account_report(entries):
    incoming = credits(entries)
    outgoing = debits(entries)
    current = incoming - outgoing
    print(f"Credits: {incoming}")
    print(f"Debits: {outgoing}")
    print(f"Current balance: {current}")
    return current

account_report([200, -80, 50, -15])

def transaction_count(transactions):
    count = 0
    for amount in transactions:
        if amount != 0:
            count += 1
    return count

print(f"Transactions: {transaction_count([100, -25, 40, -10])}")
