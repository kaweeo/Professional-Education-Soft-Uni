
minutes_walk = float(input())
walks_count = float(input())
calories_taken = float(input())

calories_burned_per_walk = minutes_walk * 5
calories_burned_per_day = calories_burned_per_walk * walks_count
calories_burned_per_day = int(calories_burned_per_day)

if calories_taken * 0.5 <= calories_burned_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned_per_day}.")