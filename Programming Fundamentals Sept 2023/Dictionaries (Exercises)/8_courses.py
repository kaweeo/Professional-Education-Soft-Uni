courses_dict = {}

while True:
    command = input()
    if command == "end":
        break
    course_record = command.split(" : ")
    course = course_record[0]
    student = course_record[1]

    if course in courses_dict.keys():
        courses_dict[course].append(student)
    else:
        courses_dict[course] = [student]

#print(courses_dict)
for k, v in courses_dict.items():
    print(f"{k}: {len(v)}")
    for student in v:
        print(f"-- {student}")