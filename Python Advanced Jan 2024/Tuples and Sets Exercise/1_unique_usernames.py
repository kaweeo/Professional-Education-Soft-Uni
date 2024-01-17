
n = int(input())

set_of_names = set()

for _ in range(n):
    set_of_names.add(input())

print("\n".join(set_of_names))

# print(*{input() for _ in range(int(input()))}, sep="\n")
