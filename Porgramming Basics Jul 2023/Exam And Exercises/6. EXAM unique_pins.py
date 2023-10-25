
n1 = int(input())
n2 = int(input())
n3 = int(input())

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        for k in range(1, n3 + 1):
            is_valid_1 = i % 2 == 0 and k % 2 == 0
            if is_valid_1:
                if all(j % divisor != 0 for divisor in range(2, int(j ** 0.5) + 1)) and 2 <= j < 8:
                    is_valid_2 = True
                    if is_valid_1 and is_valid_2:
                        print(f"{i} {j} {k}")

