from collections import deque

times_for_task_deque = deque(int(el) for el in input().split())
number_of_tasks_stack = [int(el) for el in input().split()]

ducks_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times_for_task_deque and number_of_tasks_stack:
    first_time = times_for_task_deque.popleft()
    last_tasks = number_of_tasks_stack.pop()

    time_tasks_calc = first_time * last_tasks

    if 0 <= time_tasks_calc <= 60:
        ducks_dict["Darth Vader Ducky"] += 1
    elif 61 <= time_tasks_calc <= 120:
        ducks_dict["Thor Ducky"] += 1
    elif 121 <= time_tasks_calc <= 180:
        ducks_dict["Big Blue Rubber Ducky"] += 1
    elif 181 <= time_tasks_calc <= 240:
        ducks_dict["Small Yellow Rubber Ducky"] += 1
    elif time_tasks_calc > 240:
        last_tasks -= 2
        number_of_tasks_stack.append(last_tasks)
        times_for_task_deque.append(first_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f'Darth Vader Ducky: {ducks_dict["Darth Vader Ducky"]}\nThor Ducky: {ducks_dict["Thor Ducky"]}\n'
      f'Big Blue Rubber Ducky: {ducks_dict["Big Blue Rubber Ducky"]}\n'
      f'Small Yellow Rubber Ducky: {ducks_dict["Small Yellow Rubber Ducky"]}')


