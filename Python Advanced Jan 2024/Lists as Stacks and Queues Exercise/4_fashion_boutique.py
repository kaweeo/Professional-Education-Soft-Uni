from collections import deque

box_of_clothes = deque([int(element) for element in input().split(' ')])
cap_one_rack = int(input())

racks_counter = 0
sum_clothes = 0

while len(box_of_clothes) > 0:
    piece_of_clothing = box_of_clothes.pop()
    if sum_clothes + piece_of_clothing < cap_one_rack:
        sum_clothes += piece_of_clothing
    elif sum_clothes + piece_of_clothing == cap_one_rack:
        sum_clothes = 0
        racks_counter += 1
    else:
        racks_counter += 1
        sum_clothes = piece_of_clothing

if sum_clothes > 0:
    racks_counter += 1

print(racks_counter)