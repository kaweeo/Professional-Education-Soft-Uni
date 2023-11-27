
a_players_count = 11
b_players_count = 11

cards = input()
cards_list = cards.split(" ")

a_banished_players = []
b_banished_players = []
flag = False

for card in cards_list:
    card = card.split("-")
    if card[0] == "A":
        if card[1] not in a_banished_players:
            a_banished_players.append(card[1])
            a_players_count -= 1
    elif card[0] == "B":
        if card[1] not in a_banished_players:
            b_banished_players.append(card[1])
            b_players_count -= 1
    if a_players_count < 7 or b_players_count < 7:
        flag = True
        break

print(f"Team A - {a_players_count}; Team B - {b_players_count}")
if flag == True:
    print("Game was terminated")


