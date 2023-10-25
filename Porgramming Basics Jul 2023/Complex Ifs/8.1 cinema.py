projection = input()
r = int(input())
c = int(input())

if projection == "Premiere":
    ticket = 12.00
elif projection == "Normal":
    ticket = 7.5
elif projection == "Discount":
    ticket = 5.00

places = r * c
profit = places * ticket
print(f"{profit:.2f} leva")