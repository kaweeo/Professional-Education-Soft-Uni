
count_lines = int(input())

my_chemical_set = set()

for chem_el in range(count_lines):
    chem_el = input().split(" ")
    for el in chem_el:
        my_chemical_set.add(el)

print(*my_chemical_set, sep="\n")