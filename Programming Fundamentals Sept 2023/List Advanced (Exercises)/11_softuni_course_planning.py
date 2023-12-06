
schedule_of_lessons = input().split(", ")

while True:
    modify_command = input()
    if modify_command == "course start":
        break
    modify_command = modify_command.split(":")
    if modify_command[0] == "Add":
        if not modify_command[1] in schedule_of_lessons:
            schedule_of_lessons.append(modify_command[1])
    elif modify_command[0] == "Insert":
        if not modify_command[1] in schedule_of_lessons:
            schedule_of_lessons.insert(int(modify_command[2]), modify_command[1])
    elif modify_command[0] == "Remove":
        schedule_of_lessons.remove(modify_command[1])
    elif modify_command[0] == "Swap":
        if modify_command[1] and modify_command[2] in schedule_of_lessons:
            index1 = schedule_of_lessons.index(modify_command[1])
            index2 = schedule_of_lessons.index(modify_command[2])
            schedule_of_lessons[index1], schedule_of_lessons[index2] = schedule_of_lessons[index2], schedule_of_lessons[index1]
        if f"{modify_command[1]}:Exercise" in schedule_of_lessons:
           # index_to_move = schedule_of_lessons.index(f"{modify_command[1]}:Exercise")
            schedule_of_lessons.remove(f"{modify_command[1]}:Exercise")
            index_to_follow = schedule_of_lessons.index(modify_command[1])
            schedule_of_lessons.insert(index_to_follow + 1, f"{modify_command[1]}:Exercise")
        if f"{modify_command[2]}:Exercise" in schedule_of_lessons:
           # index_to_move_2 = schedule_of_lessons.index(f"{modify_command[2]}:Exercise")
            schedule_of_lessons.remove(f"{modify_command[2]}:Exercise")
            index_to_follow_2 = schedule_of_lessons.index(modify_command[2])
            schedule_of_lessons.insert(index_to_follow_2 + 1, f"{modify_command[2]}:Exercise")

    elif modify_command[0] == "Exercise":
        if modify_command[1] in schedule_of_lessons:
            if not f"{modify_command[1]}:Exercise" in schedule_of_lessons:
                index_lecture = schedule_of_lessons.index(modify_command[1])
                schedule_of_lessons.insert(index_lecture + 1, f"{modify_command[1]}:Exercise")
        elif modify_command[1] not in schedule_of_lessons:
            schedule_of_lessons.append(modify_command[1])
            schedule_of_lessons.append(f"{modify_command[1]}:Exercise")

schedule_of_lessons = [item.replace(":", "-") if ":" in item else item for item in schedule_of_lessons]
for element in schedule_of_lessons:
    print(f"{schedule_of_lessons.index(element) + 1}.{element}")

