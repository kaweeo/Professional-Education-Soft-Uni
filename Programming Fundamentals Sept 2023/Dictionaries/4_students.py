
students = []

while True:
    record = input().split(":")
    if len(record) < 2:
        selected_course = str(record[0])
        break

    name = record[0]
    id = int(record[1])
    course = record[2]
    students.append({"name": name, "id": id, "course": course})

for student in students:
    if student["course"].startswith(selected_course[:3]):
        print(f"{student['name']} - {student['id']}")
