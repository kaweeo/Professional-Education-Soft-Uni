
weight = int(input())
hight = int(input())
tot_pieces = weight * hight
pieces_counter = 0
piece_or_stop = input()

while piece_or_stop != "STOP":
    piece_or_stop = int(piece_or_stop)
    pieces_counter += piece_or_stop
    if pieces_counter >= tot_pieces:
        diff_prices = pieces_counter - tot_pieces
        print(f"No more cake left! You need {diff_prices} pieces more.")
        break
    piece_or_stop = input()
if piece_or_stop == "STOP":
    diff_prices = tot_pieces - pieces_counter
    print(f"{diff_prices} pieces are left.")

