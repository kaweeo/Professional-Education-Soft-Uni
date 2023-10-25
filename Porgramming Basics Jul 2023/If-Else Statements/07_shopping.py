budget = float(input())
N = int(input())
M = int(input())
P = int(input())

N_price = 250
N_sum = N_price * N
M_price = 0.35 * N_sum
P_price = 0.1 * N_sum

total = N * N_price + M * M_price + P * P_price
if N > M:
    total = total * 0.85

if budget > total:
    diff = budget - total
    print(f"You have {diff:.2f} leva left!")
else:
    diff = total - budget
    print(f"Not enough money! You need {diff:.2f} leva more!")