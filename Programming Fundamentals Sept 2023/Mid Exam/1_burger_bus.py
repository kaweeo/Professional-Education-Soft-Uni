number_of_cities = int(input())

total_profit = 0


for city in range(1, number_of_cities + 1):
    city_name = input()
    city_income = float(input())
    city_expenses = float(input())



    if city % 3 == 0 and not city % 5 == 0:
        city_expenses += city_expenses * 0.5

    elif city % 5 == 0:
         city_income *= 0.9

    city_profit = city_income - city_expenses
    total_profit += city_profit

    print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")