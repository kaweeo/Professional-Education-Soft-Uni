from collections import deque

kids_names = input().split()
n_th = int(input())
def hot_potato(kids, n):
    circle = deque(kids)

    while len(circle) > 1:
        # Perform n-1 rotations (passes) without removing any kid
        for _ in range(n - 1):
            circle.rotate(-1)

        # Remove the kid at the front of the circle (the nth kid)
        removed_kid = circle.popleft()
        print(f"Removed {removed_kid}")

    # Print the last remaining kid
    last_kid = circle.pop()
    print(f"Last is {last_kid}")

hot_potato(kids_names, n_th)