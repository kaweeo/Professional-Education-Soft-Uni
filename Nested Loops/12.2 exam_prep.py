
score_counter = 0
total_score = 0
fair_score_counter = 0
fair_scores_threshold = int(input())
has_failed = True
last_test = ""

while fair_score_counter < fair_scores_threshold:
    test_name = input()
    if  test_name == "Enough":
        has_failed = False
        break

    score = int(input())
    if score <= 4:
        fair_score_counter += 1
    score_counter += 1
    total_score += score
    avg_score = total_score / score_counter
    last_test = test_name
if has_failed:
    print(f"You need a break, {fair_score_counter} poor grades.")
else:
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {score_counter}")
    print(f"Last problem: {last_test}")



