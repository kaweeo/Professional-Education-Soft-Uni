
electrons = int(input())
# shell = 2 * n ** 2
n = 1
shells = []

eletrcons_left = electrons

while eletrcons_left > 0:
    shell = 2 * n ** 2
    if shell > eletrcons_left:
        shells.append(eletrcons_left)
        break
    shells.append(shell)
    n += 1
    eletrcons_left -= shell

print(shells)

