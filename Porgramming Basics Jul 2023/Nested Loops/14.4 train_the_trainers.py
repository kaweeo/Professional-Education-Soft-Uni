n = int(input())
presentation_name = input()
presentation_counter = 0
overall_score = 0

while True:
    if presentation_name == "Finish":
        print(f"Student's final assessment is {overall_avg:.2f}.")
        break
    else:
        presentation_score = 0
        for score in range(1, n + 1):
            score = float(input())
            presentation_score += score
            overall_score += score
        avg_score = presentation_score / n
        presentation_counter += 1
        print(f"{presentation_name} - {avg_score:.2f}.")
        overall_avg = overall_score / (presentation_counter * n)
    presentation_name = input()

