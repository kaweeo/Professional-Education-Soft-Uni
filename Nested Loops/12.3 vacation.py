vac_cost = float(input())
total = float(input())
spend_counter = 0
save_counter = 0
days_counter = 0

while True:
    act = str(input())
    sum = float(input())
    days_counter += 1
    if act == "spend":
        spend_counter += 1
        total = 0
    else:
        total += sum
        spend_counter = 0
    if spend_counter == 5:
        print("You can't save the money.")
        print(f"{days_counter}")
        break
    if total >= vac_cost:
        print(f"You saved the money for {days_counter} days.")
        break

###################################################################################################################

needed_money = float(input())
init_money = float(input())

count_spend_days = 0
count_total_days = 0
total_sum = init_money
while total_sum < needed_money:
    if count_spend_days == 5:
        break

    action = input()
    amount = float(input())

    count_total_days += 1

    if action == "spend":
        count_spend_days += 1
        total_sum = total_sum - amount
        if total_sum < 0:
            total_sum = 0
    else:
        count_spend_days = 0
        total_sum = total_sum + amount

if count_spend_days == 5:
    print("You can't save the money.")
    print(count_total_days)
else:
    print(f"You saved the money for {count_total_days} days.")