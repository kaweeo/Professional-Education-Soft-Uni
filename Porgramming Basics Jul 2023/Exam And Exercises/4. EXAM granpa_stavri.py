
n = int(input())
total_liters = 0
tot_sum_degree = 0

for day in range(1, n + 1):
    rakia = float(input())
    degree = float(input())
    total_liters += rakia
    daily_sum_degree = rakia * degree
    tot_sum_degree += daily_sum_degree

avg_degree = tot_sum_degree / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {avg_degree:.2f}")

if avg_degree < 38:
    print("Not good, you should baking!")
elif 38 <= avg_degree <= 42:
    print("Super!")
elif avg_degree > 42:
    print("Dilution with distilled water!")