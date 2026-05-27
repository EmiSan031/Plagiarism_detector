def total_subscriptions(plans):
    result = 0
    for item in plans:
        result = result + item["monthly"]
    return result

def average_subscriptions(plans):
    count = 0
    total = 0
    for item in plans:
        count += 1
        total += item["monthly"]
    if count == 0:
        return 0
    return total / count

def maximum_subscriptions(plans):
    if not plans:
        return None
    best = plans[0]
    for item in plans[1:]:
        if item["monthly"] > best["monthly"]:
            best = item
    return best

def select_subscriptions(plans, minimum):
    selected = []
    for item in plans:
        if item["monthly"] >= minimum:
            selected.append(item)
    return selected

def subscription_report(plans, minimum):
    total = total_subscriptions(plans)
    average = average_subscriptions(plans)
    best = maximum_subscriptions(plans)
    selected = select_subscriptions(plans, minimum)
    print(f"Total monthly: {total}")
    print(f"Average monthly: {average:.2f}")
    print(f"Best record: {best}")
    print(f"Selected records: {selected}")
    return total, average, best, selected

data_subscriptions = [{"plan": "basic", "monthly": 9}, {"plan": "team", "monthly": 18}, {"plan": "pro", "monthly": 25}]
subscription_report(data_subscriptions, 10)
