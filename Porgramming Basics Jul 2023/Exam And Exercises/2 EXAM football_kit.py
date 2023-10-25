
shirt_price = float(input())
target_total = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = 2 * (shirt_price + shorts_price)

discount = 0.15

total_wo_disc = shirt_price + shorts_price + socks_price + shoes_price
total = total_wo_disc - total_wo_disc * discount

if total >= target_total:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total:.2f} lv.")
elif total < target_total:
    diff = abs(target_total - total)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")