time = int(input())
day = input()
working_hours = range(10, 18)

if day == "Sunday":
    print("closed")
else:
    if 10 <= time <= 18:
        print("open")
    else:
        print("closed")