odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(l) for l in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")  # B - A
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

#
# n = int(input())
# odd_set = set()
# even_set = set()
# rows = 0
#
# for name in range(n):
#     rows += 1
#     name_ord_sum = 0
#     name = input()
#     for symbol in name:
#         name_ord_sum += int(ord(symbol))
#     result_name = int(name_ord_sum / rows)
#     if result_name % 2 == 0:
#         even_set.add(result_name)
#     else:
#         odd_set.add(result_name)
#
# sum_of_odd_set = sum(odd_set)
# sum_of_even_set = sum(even_set)
#
# if sum_of_even_set == sum_of_odd_set:
#     print(", ".join(str(e) for e in odd_set.union(even_set)))
# elif sum_of_odd_set > sum_of_even_set:
#     print(", ".join(str(e) for e in odd_set.difference(even_set)))
# elif sum_of_odd_set < sum_of_even_set:
#     print(", ".join(str(e) for e in odd_set.symmetric_difference(even_set)))
