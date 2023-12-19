def check_common_values(nested_dict: dict, p1: str, p2: str) -> bool:
    if p1 in nested_dict and p2 in nested_dict:
        positions_p1 = nested_dict[p1].keys()
        positions_p2 = nested_dict[p2].keys()
         # The & operator is the set intersection operator. It returns a new set containing the common elements of the two sets.
        common_positions = set(positions_p1) & set(positions_p2)
        if common_positions:
            # print(common_positions)
            return True


def battle_looser(nested_dict: dict, p1: str, p2:str) -> None:
    if p1 and p2 in nested_dict:
        total_skill_p1 = sum(nested_dict[p1].values())
        total_skill_p2 = sum(nested_dict[p2].values())
        if total_skill_p1 == total_skill_p2:
            pass
        elif total_skill_p1 > total_skill_p2:
            nested_dict.pop(p2)
        return
        nested_dict.pop(p2)


moba_data = {}

while True:
    input_line = input()
    if input_line == 'Season end':
        break
    elif '->' in input_line:
        moba_input = input_line.split(' -> ')
        player = moba_input[0]
        position = moba_input[1]
        skill = int(moba_input[2])
        if player not in moba_data.keys():
            moba_data[player] = {position: skill}
        elif position not in moba_data[player]:
            moba_data[player].update({position: skill})
        else:
            if moba_data[player][position] < skill:
                moba_data[player] = {position: skill}
    else:
        moba_input = input_line.split(' vs ')
        player_1 = moba_input[0]
        player_2 = moba_input[1]
        if player_1 and player_2 in moba_data.keys():
            if check_common_values(moba_data, player_1, player_2):
                battle_looser(moba_data, player_1, player_2)

sorted_moba = dict(sorted(moba_data.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for k, v in sorted_moba.items():
    print(f'{k}: {sum(v.values())} skill')
    sorted_skills_player = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    for k2, v2 in sorted_skills_player.items():
        print(f'- {k2} <::> {v2}')
