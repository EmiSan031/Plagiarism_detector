def shortage_list(articles, threshold):
    names = []
    for article in articles:
        if article["amount"] <= threshold:
            names.append(article["label"])
    return names

def warehouse_value(articles):
    value = 0
    for article in articles:
        value += article["amount"] * article["unit_price"]
    return value

def warehouse_report(articles):
    short = shortage_list(articles, 4)
    value = warehouse_value(articles)
    print(f"Short items: {short}")
    print(f"Warehouse value: {value:.2f}")
    return value

articles = [{"label": "box", "amount": 3, "unit_price": 2}, {"label": "lamp", "amount": 7, "unit_price": 15}]
warehouse_report(articles)

def product_names(products):
    names = []
    for product in products:
        names.append(product.get("name", product.get("label", "")))
    return names

print(f"Products: {product_names(items) if 'items' in globals() else product_names(articles)}")
