
decor_quantity = int(input())
days_till_christmas = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

points_counter = 0
ornament_buys = 0
tree_skirt_buys = 0
tree_garland_buys = 0
tree_lights_buys = 0

for day in range(1, days_till_christmas + 1):
    if day % 2 == 0:
        ornament_buys += 1
        points_counter += ornament_set_points
    if day % 3 == 0:
        tree_skirt_buys += 1
        tree_garland_buys += 1
        points_counter += tree_skirt_points
        points_counter += tree_garland_points
    if day % 5 == 0:
        tree_lights_buys += 1
        points_counter += tree_lights_points
    if day % 3 == 0 and day % 5 == 0:
        points_counter += 30
    if day % 10 == 0:
        tree_skirt_buys += 1
        tree_garland_buys += 1
        tree_lights_buys += 1
        points_counter -= 20
    if day % 11 == 0:
        tree_skirt_buys *= 2
        tree_skirt_buys *= 2
        tree_lights_buys *= 2
        tree_garland_buys *= 2
    if day == days_till_christmas and day == 10:
        points_counter -= 30

tot_cost = ornament_buys * ornament_set_price + tree_skirt_buys * tree_skirt_price + tree_garland_buys * tree_garland_price + tree_lights_buys * tree_lights_price
print(f"Total cost: {tot_cost}")
print(f"Total spirit: {points_counter}")
