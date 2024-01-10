from collections import deque

stack = deque()

n = int(input())

for _ in range(n):
    query = input().split(' ')
    if len(query) == 2:
        _, number = query
        stack.appendleft(int(number))
    else:
        number = query[0]
        if number == '2':
            if len(stack) == 0:
                pass
            else:
                stack.popleft()
        elif number == '3':
            if len(stack) == 0:
                pass
            else:
                print(max(stack))
        elif number == '4':
            if len(stack) == 0:
                pass
            else:
                print(min(stack))

stack = list(map(lambda x: str(x), stack))
print(", ".join(stack))
