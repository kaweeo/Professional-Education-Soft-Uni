
tot_sold = int(input())

hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0

for game in range(1, tot_sold + 1):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter +=1
    elif game_name == "Fornite":
        fornite_counter +=1
    elif game_name == "Overwatch":
        overwatch_counter +=1
    else:
        others_counter +=1
procent_heartstone = hearthstone_counter / tot_sold * 100
procent_fortnite = fornite_counter / tot_sold * 100
procent_overwatch = overwatch_counter / tot_sold * 100
procent_others = others_counter / tot_sold * 100

print(f"Hearthstone - {procent_heartstone:.2f}%")
print(f"Fornite - {procent_fortnite:.2f}%")
print(f"Overwatch - {procent_overwatch:.2f}%")
print(f"Others - {procent_others:.2f}%")