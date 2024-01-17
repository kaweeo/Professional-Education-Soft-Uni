
n = int(input())

longest_intersec_set = set()

for _ in range(n):
    first_range, second_range = input().split("-") # "{first_start},{first_end}-{second_start},{second_end}"

    first_start, first_end = first_range.split(",")
    first_set = set(range(int(first_start), int(first_end) + 1))
    second_start, second_end = second_range.split(",")
    second_set = set(range(int(second_start), int(second_end) + 1))

    intersection_of_range = first_set.intersection(second_set)

    if len(intersection_of_range) > len(longest_intersec_set):
        longest_intersec_set = intersection_of_range

print(
    f"Longest intersection is [{', '.join(str(el) for el in longest_intersec_set)}] "
    f"with length {len(longest_intersec_set)}"
)

