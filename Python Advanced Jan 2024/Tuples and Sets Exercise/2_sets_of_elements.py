
n, m = input().split(" ")

n_len_set = set()
m_len_set = set()

for numb in range(int(n)):
    n_len_set.add(int(input()))

for numb in range(int(m)):
    m_len_set.add(int(input()))

# print(*n_len_set.intersection(m_len_set), sep='\n')
#
# n, m = [int(x) for x in input().split()]  # "4 3" -> ["4", "3"] -> [4, 3]
#
# first_set = {input() for _ in range(n)}   # 1, 3, 5, 7
# second_set = {input() for _ in range(m)}  # 3, 4, 5
#
# print(*first_set.intersection(second_set), sep="\n")  # 3, 5
#
# # print(first_set & second_set)  # and, intersection
# # print(first_set | second_set)  # or, union
# # print(first_set - second_set)  # subtract, difference
# # print(first_set ^ second_set)  # symmetric difference