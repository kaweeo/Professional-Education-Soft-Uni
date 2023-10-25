
days = int(input())
hours = int(input())
total_cost = 0
days_counter = 0


for day in range(1, days + 1):
    days_counter += 1
    day_cost = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_cost += 2.5
            day_cost += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_cost += 1.25
            day_cost += 1.25
        else:
            total_cost += 1
            day_cost += 1
    print(f"Day: {days_counter} - {day_cost:.2f} leva")
print(f"Total: {total_cost:.2f} leva")