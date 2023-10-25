N = int(input())  # lily age
X = float(input())  # washing machine price
P = int(input())  # toy price

money_even_bd = 0
even_bd_count = 0
toys_count = 0
for year in range(0, N + 1):
    if year % 2 == 0:
        even_bd_count += 1
        money_even_bd = money_even_bd + (even_bd_count * 10)
    else:
        toys_count += 1
money_odd_bd = toys_count * P - toys_count
total_money = money_odd_bd + money_even_bd
if total_money < X:
    M = X - total_money
    print(f"No! {M:.2f}")
else:
    diff = total_money - X
    print(f"Yes! {diff:.2f}")
