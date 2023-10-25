# "Spring", "Summer", "Autumn", "Winter"
budjet = int(input())
season = input()
fisherman_count = int(input())

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price =  4200
elif season == "Winter":
    price = 2600

if fisherman_count <= 6:
    price = price * 0.9
elif 6 < fisherman_count <= 11:
    price = price * 0.85
elif fisherman_count > 11:
    price = price * 0.75

if fisherman_count % 2 == 0:
    if season != "Autumn":
        price = price * 0.95

if price < budjet:
    leftover = budjet - price
    print(f"Yes! You have {leftover:.2f} leva left.")
elif price > budjet:
    diff = abs(price - budjet)
    print(f"Not enough money! You need {diff:.2f} leva.")