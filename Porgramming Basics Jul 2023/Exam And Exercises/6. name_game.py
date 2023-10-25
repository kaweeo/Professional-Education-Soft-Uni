
player_1_points = 0
player_2_points = 0
flag = True

while flag:
    player_1 = input()
    for letter in player_1:
        number_for_letter = int(input())
        if chr(number_for_letter) == letter:
            player_1_points += 10
        else:
            player_1_points += 2

    player_2 = input()
    for letter in player_2:
        number_for_letter = int(input())
        if chr(number_for_letter) == letter:
            player_2_points += 10
        else:
            player_2_points += 2

    flag_input = input()
    if flag_input == "Stop":
        if player_1_points > player_2_points:
            print(f"The winner is {player_1} with {player_1_points} points!")
        elif player_1_points <= player_2_points:
            print(f"The winner is {player_2} with {player_2_points} points!")
        flag = False

