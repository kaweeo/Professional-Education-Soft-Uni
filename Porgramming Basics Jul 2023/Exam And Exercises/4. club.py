dream_winning = float(input())
club_income = 0
while True:
    cocktail = input()
    if cocktail == "Party!":
        diff = abs(dream_winning - club_income)
        print(f"We need {diff:.2f} leva more.")
        print(f"Club income - {club_income:.2f} leva.")
        break
    cocktail_count = int(input())
    price = 0
    for letter in cocktail:
        price += 1
    cocktail_total = cocktail_count * price
    if cocktail_total % 2 != 0:
        cocktail_total = cocktail_total * 0.75
    club_income += cocktail_total
    if club_income >= dream_winning:
        print("Target acquired.")
        print(f"Club income - {club_income:.2f} leva.")
        break
