group_count = int(input())
all_musala_groups = 0
all_monblan_groups = 0
all_kilim_groups = 0
all_k2_groups = 0
all_everest_groups = 0

for group in range(1, group_count + 1):
    group = int(input())
    if group < 6:
        all_musala_groups += group
    elif 6 <= group < 13:
        all_monblan_groups += group
    elif 13 <= group <= 25:
        all_kilim_groups += group
    elif 25 < group <= 40:
        all_k2_groups += group
    elif 40 < group:
        all_everest_groups += group

total_count = all_musala_groups + all_monblan_groups + all_kilim_groups + all_k2_groups + all_everest_groups
all_musala_groups_pro = all_musala_groups / total_count * 100
all_monblan_groups_pro = all_monblan_groups / total_count * 100
all_kilim_groups_pro = all_kilim_groups / total_count * 100
all_k2_groups_pro = all_k2_groups / total_count * 100
all_everest_groups_pro = all_everest_groups / total_count * 100

print(f"{all_musala_groups_pro:.2f}%")
print(f"{all_monblan_groups_pro:.2f}%")
print(f"{all_kilim_groups_pro:.2f}%")
print(f"{all_k2_groups_pro:.2f}%")
print(f"{all_everest_groups_pro:.2f}%")
