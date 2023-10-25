
dancers_count = int(input())
points_won = float(input())
season = input()
place = input()

if place == "Bulgaria":
    won_money = dancers_count * points_won
    if season == "summer":
        won_money = won_money - won_money * 0.05
    elif season == "winter":
        won_money = won_money - won_money * 0.08


elif place == "Abroad":
    won_money = dancers_count * points_won
    won_money = won_money + 0.5 * won_money
    if season == "summer":
        won_money = won_money - won_money * 0.1
    elif season == "winter":
        won_money = won_money - won_money * 0.15

clear_won_money = won_money * 0.25
charity_money = won_money * 0.75
clear_money_per_dancer = clear_won_money / dancers_count

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {clear_money_per_dancer:.2f}")