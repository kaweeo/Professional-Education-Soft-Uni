factor = int(input())
count = int(input())

multiples = []

for i in range(factor, (count + 1) * factor, factor):
    multiples.append(i)

print(multiples)