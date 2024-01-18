from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

presents = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}

crafted_presents = []

while materials and magic_levels:
    last_material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    first_mag_level = magic_levels.popleft() if last_material or not magic_levels[0] else 0
    # Ternary operators: do something if condition else do something

    if not first_mag_level:
        continue

    tot_magic_level = last_material * first_mag_level

    for key, value in presents.items():
        if value == tot_magic_level:
            crafted_presents.append(key)
            break
    else:
        if tot_magic_level < 0:
            sum_mat_mag = last_material + first_mag_level
            materials.append(sum_mat_mag)
        elif tot_magic_level > 0:
            materials.append(last_material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted_presents.count(toy)}") for toy in sorted(set(crafted_presents))]
