size_of_matrix = int(input())

matrix = [[int(x) for x in input().split()] for line in range(size_of_matrix)]

primary_diagonal = [matrix[r][r] for r in range(size_of_matrix)]
secondary_diagonal = [matrix[r][size_of_matrix - r - 1] for r in range(size_of_matrix)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

#
# num = int(input())
#
# primary_sum, secondary_sum = 0, 0
# 
# for i in range(num):
#     line = [int(x) for x in input().split()]
#     primary_sum += line[i]
#     secondary_sum += line[num - i - 1]
#
# print(abs(primary_sum - secondary_sum))
