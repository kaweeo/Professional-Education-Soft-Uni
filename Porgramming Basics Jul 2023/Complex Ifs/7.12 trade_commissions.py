city = input()
volume = float(input())
cities = ["Sofia", "Varna", "Plovdiv"]
if city in cities:
    if volume < 0:
        print("error")
    else:
        if 0 <= volume <= 500:
            if city == "Sofia":
                commission = 5
            elif city == "Varna":
                commission = 4.5
            elif city == "Plovdiv":
                commission = 5.5
        elif 500 < volume <= 1000:
            if city == "Sofia":
                commission = 7
            elif city == "Varna":
                commission = 7.5
            elif city == "Plovdiv":
                commission = 8
        elif 1000 < volume <= 10000:
            if city == "Sofia":
                commission = 8
            elif city == "Varna":
                commission = 10
            elif city == "Plovdiv":
                commission = 12
        elif volume > 10000:
            if city == "Sofia":
                commission = 12
            elif city == "Varna":
                commission = 13
            elif city == "Plovdiv":
                commission = 14.5

        volume_commission = volume * commission / 100
        print(f"{volume_commission:.2f}")
else:
    print("error")
