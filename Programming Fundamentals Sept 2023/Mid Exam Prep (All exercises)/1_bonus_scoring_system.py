import math

students_count = int(input())
total_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_student_attendence = 0

for student in range(1, students_count + 1):
    student_attendance_count = int(input())
    total_bonus_per_student = student_attendance_count / total_lectures * (5 + additional_bonus)
    if total_bonus_per_student > max_bonus:
        max_bonus = total_bonus_per_student
        max_bonus_student_attendence = student_attendance_count

max_bonus = math.ceil(max_bonus)

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_bonus_student_attendence} lectures.")

