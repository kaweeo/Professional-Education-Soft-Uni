
budjet = float(input())
gender = input()
age = int(input())
sport = input()

if sport == "Gym":
    if gender == "m":
        price = 42
    elif gender == "f":
        price = 35
elif sport == "Boxing":
    if gender == "m":
        price = 41
    elif gender == "f":
        price = 37
elif sport == "Yoga":
    if gender == "m":
        price = 45
    elif gender == "f":
        price = 42
elif sport == "Zumba":
    if gender == "m":
        price = 34
    elif gender == "f":
        price = 31
elif sport == "Dances":
    if gender == "m":
        price = 51
    elif gender == "f":
        price = 53
elif sport == "Pilates":
    if gender == "m":
        price = 39
    elif gender == "f":
        price = 37

if age < 19:
    price = price * 0.8

if budjet >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = price - budjet
    print(f"You don't have enough money! You need ${diff:.2f} more.")