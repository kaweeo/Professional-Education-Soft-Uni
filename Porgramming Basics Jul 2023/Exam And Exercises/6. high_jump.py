
target_score = int(input())
starting_point = target_score - 30

jumps_count = 0
fails_count = 0
flag = True
while flag:
    for jump in range(1, 4):
        if jump == "" or " ":
            break
        else:
            jump = int(input())
            jumps_count += 1
            if jump < starting_point:
                fails_count += 1
            if fails_count == 3:
                print(f"Tihomir failed at {starting_point}cm after {jumps_count} jumps.")
                flag = False
                break
            if jump > starting_point:
                starting_point += 5
            if starting_point > target_score:
                print(f"Tihomir succeeded, he jumped over {target_score}cm after {jumps_count} jumps.")
                flag = False
                break