
days_count = int(input())
money = 0
day_winner = 0
day_looser = 0
for day in range(1, days_count + 1):
    win_count_daily = 0
    loose_count_daily = 0
    money_per_day = 0
    while True:
        game_or_finish = input()
        if game_or_finish == "Finish":
            break
        result = input()
        if result == "win":
            money_per_day += 20
            win_count_daily += 1
        else:
            loose_count_daily += 1
    if win_count_daily > loose_count_daily:
        money_per_day = money_per_day + money_per_day * 0.1
        day_winner += 1
    else:
        day_looser += 1
    money += money_per_day

if day_winner > day_looser:
    money = money + money * 0.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")