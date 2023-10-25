budget = float(input())
statists = int(input())
price_dress_per_stat = float(input())

dressing = statists * price_dress_per_stat
decor = budget * 0.1

if statists >= 150:
    dressing = dressing * 0.9

if decor + dressing > budget:
    diff = (decor + dressing) - budget
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    diff = budget - (decor + dressing)
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")