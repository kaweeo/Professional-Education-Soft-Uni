import math

time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

total_time = time_1 + time_2 + time_3
mins = total_time // 60
secs = total_time % 60
mins = math.floor(mins)

if secs < 10:
    print (f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")
