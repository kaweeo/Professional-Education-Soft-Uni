
number_of_cars = int(input())

cars_dict = {}

for car in range(number_of_cars):
    car_w_stats = input().split("|")
    car, mileage, fuel = car_w_stats[0], car_w_stats[1], car_w_stats[2]
    cars_dict[car] = {}
    cars_dict[car]["mileage"] = int(mileage)
    cars_dict[car]["fuel"] = int(fuel)

command_input = input()

while command_input != "Stop":
    command_info = command_input.split(" : ")
    command = command_info[0]
    car = command_info[1]
    if command == "Drive":
        distance = int(command_info[2])
        fuel = int(command_info[3])
        if cars_dict[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]["mileage"] += distance
            cars_dict[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]["mileage"] >= 100000:
                cars_dict.pop(car)
                print(f"Time to sell the {car}!")
    elif command == "Refuel":
        fuel_to_add = int(command_info[2])
        current_fuel = cars_dict[car]["fuel"]
        if current_fuel + fuel_to_add > 75:
            cars_dict[car]["fuel"] = 75
            added_fuel = 75 - current_fuel
        else:
            added_fuel = fuel_to_add
            cars_dict[car]["fuel"] += fuel_to_add   # to check
        print(f"{car} refueled with {added_fuel} liters")
    elif command == "Revert":
        kilometers_to_revert = int(command_info[2])
        cars_dict[car]["mileage"] -= kilometers_to_revert
        if cars_dict[car]["mileage"] < 10000:
            cars_dict[car]["mileage"] = 10000
            continue
        print(f"{car} mileage decreased by {kilometers_to_revert} kilometers")

    command_input = input()

for car, car_stats in cars_dict.items():
    print(f"{car} -> Mileage: {car_stats['mileage']} kms, Fuel in the tank: {car_stats['fuel']} lt.")
