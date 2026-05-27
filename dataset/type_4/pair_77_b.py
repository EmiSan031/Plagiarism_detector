def total_subscriptions(plans):
    return sum(map(lambda entry: entry["monthly"], plans))

def average_subscriptions(plans):
    values = tuple(entry["monthly"] for entry in plans)
    return sum(values) / len(values) if values else 0

def maximum_subscriptions(plans):
    return max(plans, key=lambda entry: entry["monthly"], default=None)

def select_subscriptions(plans, minimum):
    return list(filter(lambda entry: entry["monthly"] >= minimum, plans))

def subscription_report(plans, minimum):
    summary = (
        total_subscriptions(plans),
        average_subscriptions(plans),
        maximum_subscriptions(plans),
        select_subscriptions(plans, minimum),
    )
    labels = ("Total monthly", "Average monthly", "Best record", "Selected records")
    for label, value in zip(labels, summary):
        if isinstance(value, float):
            print(f"{label}: {value:.2f}")
        else:
            print(f"{label}: {value}")
    return summary

data_subscriptions = [{"plan": "basic", "monthly": 9}, {"plan": "team", "monthly": 18}, {"plan": "pro", "monthly": 25}]
subscription_report(data_subscriptions, 10)
