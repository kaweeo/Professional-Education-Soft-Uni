
input_line = input().split(" ")

stocks = {}

for i in range(0, len(input_line), 2):
    key = input_line[i]
    value = input_line[i + 1]
    stocks[key] = int(value)

searched_products = input().split(" ")
for product in searched_products:
    if product in stocks:
        print(f"We have {stocks[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")