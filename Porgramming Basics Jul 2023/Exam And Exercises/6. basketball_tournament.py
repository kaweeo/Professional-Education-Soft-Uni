
input_line = input()
wins = 0
losses = 0
tot_games_counter = 0

while input_line != "End of tournaments":
    num_games = int(input())
    for game in range(1, num_games + 1):
        desis_team_score = int(input())
        opponent_team_score = int(input())
        if desis_team_score > opponent_team_score:
            diff = desis_team_score - opponent_team_score
            print(f"Game {game} of tournament {input_line}: win with {diff} points.")
            wins += 1
            tot_games_counter += 1
        else:
            diff = opponent_team_score - desis_team_score
            print(f"Game {game} of tournament {input_line}: lost with {diff} points.")
            losses += 1
            tot_games_counter += 1
    input_line = input()

percentage_win = wins / tot_games_counter * 100
percentage_loss = losses / tot_games_counter * 100

print(f"{percentage_win:.2f}% matches win")
print(f"{percentage_loss:.2f}% matches lost")