exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

if arrival_hour > exam_hour:
    hour_diff = arrival_hour - exam_hour
    print("Late")
    if arrival_min > exam_min:
        min_late = arrival_min - exam_min
        print(f"{hour_diff}:{min_late} hours after the start")
    elif exam_min > arrival_min:           # JUST CHANGED SIGN
        hour_diff = hour_diff - 1
        arrival_min = 60 + arrival_min
        min_late = arrival_min - exam_min
        if hour_diff == 0:
            print(f"{min_late} minutes after the start")
        else:
            print(f"{hour_diff}:{min_late} hours after the start")
elif arrival_hour == exam_hour:
    if exam_min < arrival_min:
        print("Late")
        late = arrival_min - exam_min
        print(f"{late} minutes after the start")
    elif exam_min == arrival_min:
        print("On time")
    elif exam_min > arrival_min:
        early = exam_min - arrival_min
        if early <= 30:
            print("On time")
            print(f"{early} minutes before the start")
        elif early > 30:
            print("Early")
            print(f"{early} minutes before the start")
elif arrival_hour < exam_hour:
    diff_hour = exam_hour - arrival_hour
    if exam_min == arrival_min:
        print("Early")
        print(f"{diff_hour}:00 hours before the start")
    elif exam_min < arrival_min:
        min_early = 60 - arrival_min + exam_min           #JUST CHANGE -EXAM_MIN was + exam min
        if min_early > 30 and diff_hour == 1:
            print("Early")
            print(f"{min_early} minutes before the start")
        elif min_early > 30:
                print("Early")
                print(f"{diff_hour}:{min_early} minutes before the start")
        elif min_early <= 30 and diff_hour == 1:
            print("On time")
            print(f"{min_early} minutes before the start")
    elif exam_min > arrival_min:
        min_diff = exam_min - arrival_min
        if diff_hour == 0 and min_diff > 30:
            print("Early")
            print(f"{min_diff} minutes before the start")
        elif diff_hour == 0 and min_diff < 30:
            print("On time")
            print(f"{min_diff} minutes before the start")
        else:
            print("Early")
            print(f"{diff_hour}:{min_diff} hours before the start")
    else:
        early = exam_min - arrival_min
        print("Early")
        print(f"{early} minutes before the start")