# student = input()
# year_count = 0
# fails = 0
# total_score = 0
# flag = True
# while flag == True:
#     yearly_score = float(input())
#     year_count += 1
#     total_score += yearly_score
#     if year_count == 12:
#         flag = False
#         avg_yearly_score = total_score / year_count
#         print(f"{student} graduated. Average grade: {avg_yearly_score:.2f}")
#     if yearly_score < 4:
#         fails += 1
#     if fails == 2:
#         print(f"{student} has been excluded at {year_count - 1} grade")
#         break

student_name = input()
grades_counter = 0
years_counter = 0
failed_counter = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_counter += 1

        if failed_counter > 1:
            current_year = years_counter + 1
            print(f'{student_name} has been excluded at {current_year} grade')
            break

        continue

    else:
        grades_counter += annual_grade
        years_counter += 1

    if years_counter == 12:
        average_grade = grades_counter / 12
        print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
        break