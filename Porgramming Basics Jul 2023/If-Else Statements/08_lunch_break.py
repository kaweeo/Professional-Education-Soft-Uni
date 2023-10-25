import math

movie_name = input()
episode_time = int(input())
lunch_break = int(input())

lunch = (1/8) * lunch_break
rest = (1/4) * lunch_break
needed_time = lunch + rest

if lunch_break >= lunch + rest + episode_time:
    diff = lunch_break - (needed_time + episode_time)
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(diff)} minutes free time.")
else:
    diff = (needed_time + episode_time) - lunch_break
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(diff)} more minutes.")