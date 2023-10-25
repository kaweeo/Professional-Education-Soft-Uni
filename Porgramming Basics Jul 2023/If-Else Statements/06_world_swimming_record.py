record_s = float(input())
distance_m = float(input())
speed_ms = float(input())

slow_s = int((distance_m / 15)) * 12.5
ivans_rec = (distance_m * speed_ms) + slow_s

if ivans_rec < record_s:
    print(f" Yes, he succeeded! The new world record is {ivans_rec:.2f} seconds.")
else:
    diff = record_s - ivans_rec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")