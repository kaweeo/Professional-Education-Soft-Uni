
base = 5364
everest = 8848
tot_atanas_hiked = 0
n = 1

while True:
    will_rest_or_hike = input()
    if will_rest_or_hike == "END":
        print("Failed!")
        print(f"{atanas_reached}")  #care
        break
    if will_rest_or_hike == "Yes":
        n += 1
    if n == 6:
        print("Failed!")
        print(f"{atanas_reached}")
        break
    atanas_hiked = int(input())
    tot_atanas_hiked += atanas_hiked
    atanas_reached = tot_atanas_hiked + base
    if everest <= atanas_reached:
        print(f"Goal reached for {n} days!")
        break

