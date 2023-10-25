name = input()
starting_points = float(input())
assessor_count = int(input())

total_points = starting_points
for assessor in range(1, assessor_count + 1):
    assessor_name = input()
    assessor_s_score = float(input())
    assesors_points_alpha_count = 0
    for char in assessor_name:
        assesors_points_alpha_count += 1
    final_assesors_points = (assesors_points_alpha_count * assessor_s_score) / 2
    total_points = total_points + final_assesors_points
    if total_points >= 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {round(total_points, 1)}!")
        break
if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {name} you need {diff} more!")