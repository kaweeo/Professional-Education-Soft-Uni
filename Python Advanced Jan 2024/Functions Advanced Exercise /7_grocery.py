def grocery_store(**products):
    # dict(sorted(people.items(), key=lambda item: item[1]))
    sorted_products = dict(sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = '\n'.join([f"{k}: {v}" for k, v in sorted_products.items()])
    return result

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
