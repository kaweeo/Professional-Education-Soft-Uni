
flower = input()
count = int(input())
budjet = int(input())

rose_pr = 5
dalia_pr = 3.8
tulip_pr = 2.8
narcis_pr = 3
glad_pr = 2.5

if flower == "Roses":
    total = rose_pr * count
    if count > 80:
        total = total - total * 0.1
elif flower == "Dahlias":
    total = dalia_pr * count
    if count > 90:
        total = total - total * 0.15
elif flower == "Tulips":
    total = tulip_pr * count
    if count > 80:
        total = total - total * 0.15
elif flower == "Narcissus":
    total = narcis_pr * count
    if count < 120:
        total = total + total * 0.15
elif flower == "Gladiolus":
    total = glad_pr * count
    if count < 80:
        total = total + total * 0.20

if budjet >= total:
    leftover = budjet - total
    print(f"Hey, you have a great garden with {count} {flower} and {leftover:.2f} leva left.")
else:
    leftover = total - budjet
    print(f"Not enough money, you need {leftover:.2f} leva more.")