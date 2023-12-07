
ratings_list = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()

entry_index = entry_point
entry_value = ratings_list[entry_index]

items_left = ratings_list[:entry_index]
items_right = ratings_list[entry_index + 1:]        #[entry_index:]

if type_of_items == "cheap":
    damaged_items_left = [item for item in items_left if item < entry_value]
    damaged_items_right = [item for item in items_right if item < entry_value]

elif type_of_items == "expensive":     #care here for tests passing
    damaged_items_left = [item for item in items_left if item >= entry_value]
    damaged_items_right = [item for item in items_right if item >= entry_value]

sum_damaged_items_left = sum(damaged_items_left)
sum_damaged_items_right = sum(damaged_items_right)

#print(sum_damaged_items_right, sum_damaged_items_right)

if sum_damaged_items_right > sum_damaged_items_left:
    position = "Right"
    sum_price = sum_damaged_items_right
else:
    position = "Left"
    sum_price = sum_damaged_items_left
print(f"{position} - {sum_price}")