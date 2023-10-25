
Increase = ""
total = 0
while True:
    Increase = input()
    if Increase == "NoMoreMoney":
        break
    if float(Increase) < 0:
        print("Invalid operation!")
        break
    total += float(Increase)
    print(f"Increase: {float(Increase):.2f}")

print(f"Total: {total:.2f}")

