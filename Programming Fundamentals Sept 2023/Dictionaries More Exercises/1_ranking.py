contests_w_passes = {}
users_dict = {}


def contest_is_valid(contest_exam: str) -> bool:
    return contest_exam in contests_w_passes.keys()


def password_is_valid(pass_word: str) -> bool:
    return pass_word in contests_w_passes.values()


while True:
    data_input = input()
    if data_input == 'end of contests':
        break
    contest_with_password = data_input.split(':')
    contest = contest_with_password[0]
    passwd = contest_with_password[1]
    contests_w_passes[contest] = passwd

while True:
    data_input = input()
    if data_input == 'end of submissions':
        break
    submission = data_input.split("=>")
    contest = submission[0]
    passwd = submission[1]
    username = submission[2]
    points = submission[3]

    if contest_is_valid(contest) and password_is_valid(passwd):
        if username in users_dict:
            if contest in users_dict[username]:
                if int(points) > int(users_dict[username][contest]):
                    users_dict[username][contest] = points
            else:
                users_dict[username][contest] = points
        else:
            users_dict[username] = {contest: points}

max_points = -1000000
best_user = None

for user, contests in users_dict.items():  # user with max points
    total_points = sum(int(points) for points in contests.values())
    if total_points > max_points:
        best_user = user
        max_points = total_points

# Print the best user after the loop if it is defined
if best_user is not None:
    print(f"Best candidate is {best_user} with total {max_points} points.")
    print('Ranking:')

    # Sort by items in the main dict
    users_dict = dict(sorted(users_dict.items()))

    for user, contest in users_dict.items():
        print(f'{user}')
        sorted_contests = dict(sorted(contest.items(), key=lambda x: int(x[1]), reverse=True))
        for contst, points in sorted_contests.items():
            print(f'#  {contst} -> {points}')