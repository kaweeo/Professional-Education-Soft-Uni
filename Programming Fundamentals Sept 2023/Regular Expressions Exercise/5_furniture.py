import re
orders = []
pattern = r'>>(.*?)<<([0-9]+\.*[0-9]+)!(\d+)'
total_cost = 0
bought_furniture = []
while True:
    order = input()
    if order == 'Purchase':
        break
    match = re.search(pattern, order)
    if match:
        furniture, price, quantity = match.groups()
        #print(furniture, price, quantity)
        total_cost += float(price) * int(quantity)
        bought_furniture.append(furniture)

print('Bought furniture:')
for furniture in bought_furniture:

    print(f'{furniture}')
print(f'Total money spend: {total_cost:.2f}')