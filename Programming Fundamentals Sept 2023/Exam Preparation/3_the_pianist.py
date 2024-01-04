
number_of_pieces = int(input())

pianist_collection = []
piece_dict = {}

# Collection initial collection
for piece_input in range(number_of_pieces):
    piece_input = input().split("|")
    piece = piece_input[0]
    composer = piece_input[1]
    key = piece_input[2]
    piece_dict = {"piece": piece, "composer": composer, "key": key}
    pianist_collection.append(piece_dict)


while True:
    piece_already_in_collection = False
    changed_key = False
    successfully_removed = False
    input_command = input()
    if input_command == "Stop":
        break
    input_command = input_command.split("|")
    command = input_command[0]
    piece = input_command[1]
    if command == "Add":
        composer = input_command[2]
        key = input_command[3]
        for piece_dict in pianist_collection:
            if piece_dict['piece'] == piece:
                print(F"{piece} is already in the collection!")  # migh need to print descriptions as well
                piece_already_in_collection = True
                break
        if not piece_already_in_collection:
            dict_to_be_added = {"piece": piece, "composer": composer, "key": key}
            pianist_collection.append(dict_to_be_added)
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        for piece_dict in pianist_collection:
            if piece_dict['piece'] == piece:
                pianist_collection.remove(piece_dict)
                print(f"Successfully removed {piece}!")
                successfully_removed = True
                break
        if not successfully_removed:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        new_music_key = input_command[2]
        for piece_dict in pianist_collection:
            if piece_dict['piece'] == piece:
                piece_dict["key"] = new_music_key
                print(f"Changed the key of {piece} to {new_music_key}!")
                changed_key = True
                break
        if not changed_key:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece_dict in pianist_collection:
    print(f'{piece_dict["piece"]} -> Composer: {piece_dict["composer"]}, Key: {piece_dict["key"]}')