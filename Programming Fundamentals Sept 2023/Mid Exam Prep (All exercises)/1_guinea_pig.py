
food = float(input())
food *= 1000
hay = float(input())
hay *= 1000
cover = float(input())
cover *= 1000

days = 30
pigs_weight = float(input())
pigs_weight *= 1000
flag = False

for day in range(1, days+1):
    food -= 300
    if food <= 0:
        flag = True

    if day % 2 == 0:
        hay -= food * (5/100)
        if hay <= 0:
            flag = True

    if day % 3 == 0:
        cover -= pigs_weight * 1/3
        if cover <= 0:
            flag = True

    if flag:
        print("Merry must go to the pet store!")
        break

if not flag:
    print('Everything is fine! Puppy is happy! ' \
          f'Food: {food / 1000:.2f}, ' \
          f'Hay: {hay / 1000:.2f}, ' \
          f'Cover: {cover / 1000:.2f}.')