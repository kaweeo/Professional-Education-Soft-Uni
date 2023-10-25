import math

rocord_sec = float(input())
distance_m = float(input())
time_sec_per_m = float(input())

george_time = distance_m * time_sec_per_m
george_time_slow = distance_m / 50
george_time_slow = math.floor(george_time_slow)
george_time_slow = george_time_slow * 30
final_george_time = george_time + george_time_slow

if final_george_time <= rocord_sec:
    print(f" Yes! The new record is {final_george_time:.2f} seconds.")
else:
    diff = abs(final_george_time - rocord_sec)
    print(f"No! He was {diff:.2f} seconds slower.")