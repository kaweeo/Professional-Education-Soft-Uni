from collections import deque
from datetime import datetime, timedelta

robo_dict = {}

robots = input().split(";")
for robot in robots:
    robot_name, processing_time = robot.split("-")[0], robot.split("-")[1]
    robo_dict[robot_name] = [int(processing_time), 0]

time_input = input()
time = datetime.strptime(time_input, '%H:%M:%S')

products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    time += timedelta(0, 1)
    current_product = products.popleft()

    free_robots = []

    for k, v in robo_dict.items():
        if v[1] != 0:
            robo_dict[k][1] -= 1

        if v[1] == 0:
            free_robots.append([k, v])

    if not free_robots:
        products.append(current_product)
        continue

    robot_name, processing_time = free_robots[0]
    robo_dict[robot_name][1] = processing_time[0]

    print(f"{robot_name} - {current_product} [{time.strftime('%H:%M:%S')}]")

