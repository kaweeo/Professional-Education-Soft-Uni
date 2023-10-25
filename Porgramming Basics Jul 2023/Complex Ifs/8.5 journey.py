# "summer” или "winter”
budjet = float(input())
season = input()


if budjet <= 100:
    distination = "Bulgaria"
    if season == "summer":
        spent = budjet * 0.3
        stay = "Camp"
    elif season == "winter":
        spent = budjet * 0.7
        stay = "Hotel"
elif budjet <= 1000:
    distination = "Balkans"
    if season == "summer":
        spent = budjet * 0.4
        stay = "Camp"
    elif season == "winter":
        spent = budjet * 0.8
        stay = "Hotel"
elif budjet > 1000:
    distination = "Europe"
    stay = "Hotel"
    spent = budjet * 0.9

print(f"Somewhere in {distination}" )
print(f"{stay} - {spent:.2f}")


