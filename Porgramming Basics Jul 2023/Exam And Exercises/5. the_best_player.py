
the_best_score = 0
the_best_player = ""

while True:
    player = input()
    if player == "END":
        break
    score = int(input())
    if score > the_best_score:
        the_best_score = score
        the_best_player = player
    if score >= 10:
        break
print(f"{the_best_player} is the best player!")

if the_best_score >= 3:
    print(f"He has scored {the_best_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {the_best_score} goals.")