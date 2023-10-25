
fruit = input()
set_size = input()
set_count = int(input())

if fruit == "Watermelon":
    if set_size == "small":
        price = 2 * 56
    else:
        price = 5 * 28.7
elif fruit == "Mango":
    if set_size == "small":
        price = 2 * 36.66
    else:
        price = 5 * 19.60
elif fruit == "Pineapple":
    if set_size == "small":
        price = 2 * 42.10
    else:
        price = 5 * 24.80
elif fruit == "Raspberry":
    if set_size == "small":
        price = 2 * 20
    else:
        price = 5 * 15.20

tot = set_count * price

if tot < 400:
    total = tot
elif 400 <= tot <= 1000:
    tot = tot * 0.85
else:
    tot = tot * 0.5

print(f"{tot:.2f} lv.")