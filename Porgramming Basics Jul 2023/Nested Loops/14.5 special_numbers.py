
n = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_valid = n % i == 0 and n % j == 0 and n % k == 0 and n % l == 0
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")

# while True:
#     N = int(input())
#     N = str(N)
#     for numb in range(1111, 10000):
#         for digit in str(numb):                # for every digit in number
#             if str(digit) in str(numb):       # for every DIGIT in the number
#                 if int(digit) != 0:
#                     if int(N) % int(digit) == 0:
#                         print(digit)
