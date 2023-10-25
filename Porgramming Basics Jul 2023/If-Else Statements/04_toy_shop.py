puzzle_price = 2.60
talking_doll_price = 3
teddyBear_price =  4.10
minion_price = 8.20
truck_price = 2

vac_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddyBear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_order = puzzle_count * puzzle_price + talking_doll_count * talking_doll_price + teddyBear_count * teddyBear_price + minion_count * minion_price + truck_count * truck_price
toys_count = puzzle_count + talking_doll_count + teddyBear_count + minion_count + truck_count

if toys_count >= 50:
    total_order = total_order * 0.75

rent = total_order * 0.1

money_left = total_order - rent

if money_left > vac_price:
    money_left = money_left - vac_price
    money_left = round(money_left, 2)
    print(f"Yes! {money_left:.2f} lv left.")
else:
    need_more = vac_price - money_left
    need_more = round(need_more, 2)
    print(f"Not enough money! {need_more} lv needed.")
