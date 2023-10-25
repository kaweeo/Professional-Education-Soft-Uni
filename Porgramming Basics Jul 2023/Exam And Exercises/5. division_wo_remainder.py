
n = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0

for num in range (1, n + 1):
    num = int(input())
    if num % 2 == 0:
        count_p1 += 1
    if num % 3 == 0:
        count_p2 += 1
    if num % 4 == 0:
        count_p3 += 1

p1 = count_p1 / n * 100
p2 = count_p2 / n * 100
p3 = count_p3 / n * 100

print(f"{p1:.2f}% \n{p2:.2movief}% \n{p3:.2f}%")