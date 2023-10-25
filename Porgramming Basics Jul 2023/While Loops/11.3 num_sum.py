
total = int(input())
sum_num = 0
while True:
    number = int(input())
    sum_num += number
    if sum_num >= total:
        break
print(sum_num)
