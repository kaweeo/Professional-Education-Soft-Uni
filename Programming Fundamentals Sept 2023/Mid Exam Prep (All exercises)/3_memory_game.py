def invalid_indexes(input_list: list, counter: int) -> list:
    """ Checking for invalid indexes"""

    middle_index = len(input_list) // 2
    elements_to_insert = f"-{counter}a"
    # Create a new list with the elements inserted in the middle
    list = input_list[:middle_index] + [elements_to_insert, elements_to_insert] + input_list[middle_index:]

    print("Invalid input! Adding additional elements to the board")
    return list


def board_checker(input_list: list) -> bool:
    """ Checking is the game done, when all ints are removed from the list"""
    return len(input_list) == 0


list = input().split(" ")
moves_counter = 0

while True:
    command = input()
    if command == "end":
        print(f"Sorry you lose :(\n{' '.join(list)}")
        break

    else:
        command = command.split(" ")
        index1 = int(command[0])
        index2 = int(command[1])
        moves_counter +=1
        if index1 == index2:
            list = invalid_indexes(list, moves_counter)
        elif index1 < 0 or index2 < 0:
            list = invalid_indexes(list, moves_counter)
        elif index1 >= len(list) or index2 >= len(list):
            list = invalid_indexes(list, moves_counter)
        elif list[index1] == list[index2]:
            print(f"Congrats! You have found matching elements - {list[index1]}!")
            second_element = list[index2]
            list.pop(index1)
            list.remove(second_element)
        elif list[index1] != list[index2]:
            print("Try again!")

        if board_checker(list):
            print(f"You have won in {moves_counter} turns!")
            break

#
# # 3 Memory Game:
# sequence = input().split(" ")
# counter = 0
#
# while True:
#     command = input()
#     if command == "end":
#         break
#     counter += 1
#     string = command.split(" ")
#     left = int(string[0])
#     right = int(string[1])
#     if left == right or 0 > left or left >= len(sequence) or 0 > right or right >= len(sequence):
#         print(f"Invalid input! Adding additional elements to the board")
#         mid_point = len(sequence) // 2
#         sequence.insert(mid_point, f"-{counter}a")
#         sequence.insert(mid_point, f"-{counter}a")
#     else:
#         if sequence[left] == sequence[right]:
#             left_item_to_remove = sequence[left]
#             sequence.remove(left_item_to_remove)
#             sequence.remove(left_item_to_remove)
#             print(f"Congrats! You have found matching elements - {left_item_to_remove}!")
#         else:
#             print(f"Try again!")
#     if len(sequence) == 0:
#         print(f"You have won in {counter} turns!")
#         break
#
# if len(sequence) > 0:
#     print(f"Sorry you lose :(")
#     print(*sequence)