number_of_students = int(input())

students = {}

for student in range(number_of_students):
    # name, grade = input().split(" ")
    name_and_grade = input().split(" ")
    name = name_and_grade[0]
    grade = float(name_and_grade[1])
    if name in students:
        students[name] += (grade, )
    else:
        students[name] = (grade, )

for k, v in students.items():
    formatted_values = ' '.join("{:.2f}".format(val) for val in v)
    print(f"{k} -> {formatted_values} (avg: {sum(v) / len(v):.2f})")
