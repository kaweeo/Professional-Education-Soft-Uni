
rent = int(input())

cake = rent * 0.2
drinks = cake - (cake * 0.45)
animator = 1/3 * rent

total = rent + cake + drinks + animator
print(f"{total:.1f}")