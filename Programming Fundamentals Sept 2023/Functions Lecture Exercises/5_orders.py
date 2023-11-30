
def order_calculator(product: str, quantity: int) -> float:
    if product == "coffee":
        product_price = 1.5
    elif product == "water":
        product_price = 1
    elif product == "coke":
        product_price = 1.4
    total_oder = product_price * quantity
    return total_oder

order_product = input()
order_quantity = int(input())

result = order_calculator(order_product, order_quantity)
print(f"{result:.2f}")