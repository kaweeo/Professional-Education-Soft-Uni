from collections import deque

conquered_peaks = []
food_supplies_stack = [int(x) for x in input().split(", ")]
daily_stamina_deque = deque([int(x) for x in input().split(", ")])

mountain_picks_dict = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

for day in range(7):
    if len(mountain_picks_dict.keys()) == 0:
        break
    last_food = food_supplies_stack.pop()
    first_stamina = daily_stamina_deque.popleft()

    alex_sum = last_food + first_stamina
    current_pick = list(mountain_picks_dict.items())[0]

    if alex_sum >= current_pick[1]:
        conquered_peaks.append(current_pick[0])
        del mountain_picks_dict[current_pick[0]]

if len(mountain_picks_dict.keys()) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))
