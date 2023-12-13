
exam_dict = {}
lang_submissions_dict = {}

while True:
    command = input()
    if command == "exam finished":
        break
    record = command.split("-")
    username = record[0]
    language = record[1]
    if record[1] == "banned":
        banned_user = username
        if banned_user in exam_dict.keys():
            del exam_dict[banned_user]
        continue
    else:
        points = record[2]

    if not language in lang_submissions_dict.keys():
        lang_submissions_dict[language] = 0
        lang_submissions_dict[language] += 1

    if not username in exam_dict:
        exam_dict[username] = {}
        exam_dict[username][language] = points

    elif username in exam_dict and language in exam_dict[username]:
        if exam_dict[username][language] < points:
            exam_dict[username][language] = points

    elif username in exam_dict and language not in exam_dict[username]:
        exam_dict[username][language] = points

print("Results:")
for username, points in exam_dict.items():
    print(f"{username} | {', '.join(f'{value}' for language, value in points.items())}")
print("Submissions:")
for language, submissions in lang_submissions_dict.items():
    print(f"{language} - {submissions}")