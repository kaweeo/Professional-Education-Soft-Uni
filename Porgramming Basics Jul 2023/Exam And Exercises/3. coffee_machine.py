city = input()
package_type = input()
vip = input()
days_count = int(input())

if days_count < 1:
    print("Days must be positive number!")
else:
    if city == "Bansko" or city == "Borovets":
        if package_type == "noEquipment":
            price = 80
            if vip == "yes":
                price = price * 0.95
        elif package_type == "withEquipment":
            price = 100
            if vip == "yes":
                price = price * 0.90
        tot = price * days_count
        print(f"The price is {tot:.2f}lv! Have a nice time!")
    elif city == "Varna" or city == "Burgas":
        if package_type == "withBreakfast":
            price = 130
            if vip == "yes":
                price = price * 0.88
        elif package_type == "noBreakfast":
            price = 100
            if vip == "yes":
                price = price * 0.93
        tot = price * days_count
        print(f"The price is {tot:.2f}lv! Have a nice time!")
    else:
        print("Invalid input!")



