items_dict = {}

while True:
    comand = input()
    if comand == "buy":
        break
    command = comand.split(" ")
    item = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if not item in items_dict.keys():
        items_dict[item] = {'price': price, 'quantity': quantity}
    else:
        items_dict[item]["quantity"] += quantity
        items_dict[item]["price"] = price

for k, v in items_dict.items():
    total_price = items_dict[k]["quantity"] * items_dict[k]["price"]
    print(f"{k} -> {total_price:.2f}")
   