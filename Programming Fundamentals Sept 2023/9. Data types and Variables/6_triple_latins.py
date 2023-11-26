# chr(ord(97))     97:122
num = int(input())

for i in range(num):
    for j in range(num):
        for k in range(num):
            print(chr(ord('a') + i) + chr(ord('a') + j) + chr(ord('a') + k))



