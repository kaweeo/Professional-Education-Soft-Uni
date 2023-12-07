def slicer(items_list: list, index: int) -> list:
    items_left = items_list[:index]
    items_right = items_list[index + 1:]  # [entry_index:]
    return items_right, items_left


def damage_calculator(type: str, value:int, list_left:list, list_right:list) -> list:
    if type == "cheap":
        damaged_items_left = [item for item in list_left if item < value]
        damaged_items_right = [item for item in list_right if item < value]

    else:
        damaged_items_left = [item for item in list_left if item >= value]
        damaged_items_right = [item for item in list_right if item >= value]

    sum_damaged_items_left = sum(damaged_items_left)
    sum_damaged_items_right = sum(damaged_items_right)

    return sum_damaged_items_right, sum_damaged_items_left


def result_returner(sum_right: int, sum_left: int, ):
    if sum_right > sum_left:
        position = "Right"
        sum_price = sum_damaged_items_right
    else:
        position = "Left"
        sum_price = sum_damaged_items_left

    result = f"{position} - {sum_price}"
    return result

ratings_list = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()
entry_index = entry_point
entry_value = ratings_list[entry_index]

items_right, items_left = slicer(ratings_list, entry_point)
sum_damaged_items_right, sum_damaged_items_left = damage_calculator(type_of_items, entry_value, items_left, items_right)
print(result_returner(sum_damaged_items_right, sum_damaged_items_left))









