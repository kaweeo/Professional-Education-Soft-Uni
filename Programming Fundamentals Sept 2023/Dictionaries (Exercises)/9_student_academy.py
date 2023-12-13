
n = int(input())

gradebook = {}

for student in range(n):
    student_name = input()
    score = float(input())
    if student_name in gradebook.keys():
        gradebook[student_name].append(score)
    else:
        gradebook[student_name] = [score]

for k, v in gradebook.items():
    avg_score = sum(v) / len(v)
    if avg_score >= 4.5:
        print(f"{k} -> {avg_score:.2f}")