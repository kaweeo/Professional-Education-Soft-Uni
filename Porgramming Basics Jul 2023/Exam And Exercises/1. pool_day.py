budjet = float(input())
nights_count = int(input())
price_per_night = float(input())
additinal_spending_percent = int(input())

if nights_count > 7:
    price_per_night = price_per_night * 0.95

tot_cost = nights_count * price_per_night + budjet * additinal_spending_percent / 100

if budjet >= tot_cost:
    leftover = abs(budjet - tot_cost)
    print(f"Ivanovi will be left with {leftover:.2f} leva after vacation.")
else:
    leftover = abs(tot_cost- budjet)
    print(f"{leftover:.2f} leva needed.")