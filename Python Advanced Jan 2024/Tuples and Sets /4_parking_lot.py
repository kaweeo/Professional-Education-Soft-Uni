
n = int(input())

set_of_cars = set()

for car in range(n):
    direction_car_number = input().split(", ")
    direction = direction_car_number[0]
    car_number = direction_car_number[1]
    if direction == "IN":
        set_of_cars.add(car_number)
    else:
        set_of_cars.remove(car_number)
if len(set_of_cars) == 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(set_of_cars))