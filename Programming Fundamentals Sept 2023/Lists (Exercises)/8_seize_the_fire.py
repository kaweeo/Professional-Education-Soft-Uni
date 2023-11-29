input_string = input()
water = int(input())

effort = 0
fire = 0
cells = []

input_list = input_string.split("#")

for element in input_list:
    fire_stats = element.split()
    type_of_fire = fire_stats[0]
    cells_value = int(fire_stats[2])
    if type_of_fire == "High":
        range_of_fire = range(81, 126, 1)
    elif type_of_fire == "Medium":
        range_of_fire = range(51, 81, 1)
    elif type_of_fire == "Low":
        range_of_fire = range(1, 51, 1)

    if cells_value in range_of_fire:
        if cells_value <= water:
            fire += cells_value
            water -= cells_value
            effort += cells_value * 0.25
            cells.append(cells_value)

print("Cells:")
for cell in cells:
    print(" -", cell)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")