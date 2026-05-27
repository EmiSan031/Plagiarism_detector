def total_subscriptions(plans):
    total = 0
    for item in plans:
        total += item["monthly"]
    return total

def average_subscriptions(plans):
    if not plans:
        return 0
    return total_subscriptions(plans) / len(plans)

def high_subscriptions(plans, minimum):
    selected = []
    for item in plans:
        if item["monthly"] >= minimum:
            selected.append(item)
    return selected

def subscription_report(plans, minimum):
    total = total_subscriptions(plans)
    average = average_subscriptions(plans)
    selected = high_subscriptions(plans, minimum)
    print(f"Records         : {plans}")
    print(f"Total monthly  : {total}")
    print(f"Average monthly: {average:.2f}")
    print(f"Selected        : {len(selected)}")
    return selected

example_subscriptions = [{"plan": "basic", "monthly": 9, "users": 14}, {"plan": "team", "monthly": 18, "users": 8}]
subscription_report(example_subscriptions, 10)
