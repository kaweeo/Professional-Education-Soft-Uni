employs = input().split(" ")
factor_of_happiness = int(input())

employs = [int(employee) for employee in employs]
happiness_boosted_employs = [employee * factor_of_happiness for employee in employs]

avg_happiness = sum(happiness_boosted_employs) / len(happiness_boosted_employs)
happy_employs = [happy_employ for happy_employ in happiness_boosted_employs if happy_employ > avg_happiness]
happy_count = int(len(happy_employs))
total_count = len(employs)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")