n = int(input())
salary = int(input())

for name in range(1, n + 1):
    if salary <= 0:
        print("You have lost your salary.")
        break
    elif salary > 0:
        name = input()
        if name == "Facebook":
            salary = salary - 150
        elif name == "Instagram":
            salary = salary - 100
        elif name == "Reddit":
            salary = salary - 50
if salary > 0:
    print(salary)
