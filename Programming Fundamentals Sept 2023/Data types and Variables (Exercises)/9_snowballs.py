n = int(input())
highest_snowball_value = 0

for snowball in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight / time_needed) ** quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        snowball_weight = weight
        snowball_time = time_needed
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(highest_snowball_value)} ({snowball_quality})")