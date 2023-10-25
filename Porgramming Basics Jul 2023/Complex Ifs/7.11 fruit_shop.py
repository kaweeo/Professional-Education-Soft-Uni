fruit = input()
day = input()
quantity = float(input())

working = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

if fruit in fruits:
    if day in working:
        if fruit == "banana":
            fruit_price = 2.50
        elif fruit == "apple":
            fruit_price = 1.2
        elif fruit == "orange":
            fruit_price = 0.85
        elif fruit == "grapefruit":
            fruit_price = 1.45
        elif fruit == "kiwi":
            fruit_price = 2.7
        elif fruit == "pineapple":
            fruit_price = 5.5
        elif fruit == "grapes":
            fruit_price = 3.85
        bill = quantity * fruit_price
        print(f"{bill:.2f}")
    elif day in weekend:
        if fruit == "banana":
            fruit_price = 2.70
        elif fruit == "apple":
            fruit_price = 1.25
        elif fruit == "orange":
            fruit_price = 0.9
        elif fruit == "grapefruit":
            fruit_price = 1.6
        elif fruit == "kiwi":
            fruit_price = 3
        elif fruit == "pineapple":
            fruit_price = 5.6
        elif fruit == "grapes":
            fruit_price = 4.2
        bill = quantity * fruit_price
        print(f"{bill:.2f}")
    else:
        print("error")
else:
    print("error")



