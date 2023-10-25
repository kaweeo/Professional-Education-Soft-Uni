import math

weight = int(input())
height = int(input())
no_paint_area = int(input()) # not procent

wall = weight * height
total_area = 4 * wall
total_area = math.ceil(total_area)
total_area_to_be_painted = total_area - (total_area * (no_paint_area / 100))

painted_area = 0
# work left = ?
paint_leters = ""

while paint_leters != "Tired!":
    paint_leters = input()
    if paint_leters == "Tired!":
        diff = abs(total_area_to_be_painted - painted_area)
        print(f"{int(diff)} quadratic m left.")
        break
    paint_leters = int(paint_leters)
    painted_area += paint_leters
    if painted_area > total_area_to_be_painted:
        over_liters = painted_area - total_area_to_be_painted
        print(f"All walls are painted and you have {int(over_liters)} l paint left!")
        break
    if painted_area == total_area_to_be_painted:
        print("All walls are painted! Great job, Pesho!")
        break