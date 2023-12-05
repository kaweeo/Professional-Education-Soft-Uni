
employs = input()
factor = int(input())

employs_happiness_list = employs.split(" ")
employs_happiness = list(map(lambda x: int(x) * factor, employs_happiness_list))

filtered = list(filter(lambda x: x >= (sum(employs_happiness) / len(employs_happiness)), employs_happiness))

if len(filtered) >= len(employs_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(employs_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employs_happiness)}. Employees are not happy!")