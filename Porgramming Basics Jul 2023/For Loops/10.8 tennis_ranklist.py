
tour_count = int(input())
starting_points = int(input())
achivements_points = 0
count_won = 0
for tour in range(1, tour_count + 1):
    achievement = input()
    if achievement == "W":
        achivements_points += 2000
        count_won += 1
    elif achievement == "F":
        achivements_points += 1200
    elif achievement == "SF":
        achivements_points += 720

fintal_points = starting_points + achivements_points
avg_points = achivements_points / tour_count
pct_won = count_won / tour_count * 100
print(f"Final points: {fintal_points}")
print(f"Average points: {int(avg_points)}")
print(f"{pct_won:.2f}%")