from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

initial_track_len = len(fuel_needed.copy())
altitude_counter = 0
reached_altitudes = []

while initial_fuel and consumption_index and fuel_needed:
    last_fuel = initial_fuel.pop()
    first_index_value = consumption_index.popleft()
    indexed_fuel = last_fuel - first_index_value
    fuel_need_for_current_altitude = fuel_needed.popleft()
    altitude_counter += 1
    if indexed_fuel >= fuel_need_for_current_altitude:
        reached_altitudes.append(f"Altitude {str(altitude_counter)}")
        print(f"John has reached: Altitude {altitude_counter}")
    else:
        print(f"John did not reach: Altitude {altitude_counter}")
        break

if not initial_fuel and not consumption_index and not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if reached_altitudes:
        print("Reached altitudes:", end=" ")
        print(", ".join(reached_altitudes), end="")
    else:
        print("John didn't reach any altitude.")


### SOLUTION 2
# from collections import deque
#
# initial_fuel_seq = [int(x) for x in input().split()]
# additional_consumption = deque(int(x) for x in input().split())
# fuel_needed = deque(int(x) for x in input().split())
#
# altitude_counter = 0
#
# for _ in range(len(fuel_needed)):
#     result = (initial_fuel_seq.pop() - additional_consumption.popleft()) - fuel_needed.popleft()
#     if result >= 0:
#         altitude_counter += 1
#         print(f"John has reached: Altitude {altitude_counter}")
#         if altitude_counter == 4:
#             print("John has reached all the altitudes and managed to reach the top!")
#     else:
#         print(f"John did not reach: Altitude {altitude_counter + 1}")
#         if altitude_counter > 0:
#             altitudes = [f"Altitude {i}" for i in range(1, altitude_counter + 1)]
#             print(f"John failed to reach the top.\n"
#                   f"Reached altitudes: {', '.join(altitudes)}")
#         else:
#             print("John failed to reach the top.\nJohn didn't reach any altitude.")
#         break

### SOLUTION 3
# from collections import deque
#
# # Initialize altitude names
# altitude_names = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])
#
# # Read input sequences
# fuel = list(map(int, input().split()))
# consumption_index = deque(map(int, input().split()))
# needed_fuel_amount = deque(map(int, input().split()))
#
# # Initialize altitudes with values
# altitudes_with_values = {}
# for key in altitude_names:
#     if needed_fuel_amount:
#         value = needed_fuel_amount.popleft()
#         altitudes_with_values[key] = value
#
# # Initialize reached altitudes
# reached_altitudes = []
#
# # Main loop
# while fuel and consumption_index and altitudes_with_values:
#     current_level = altitude_names[0]
#     current_fuel = fuel[-1]
#     additional_consumption = consumption_index[0]
#     difference = current_fuel - additional_consumption
#
#     if difference >= altitudes_with_values[current_level]:
#         fuel.pop()
#         consumption_index.popleft()
#         reached_altitudes.append(current_level)
#         del altitudes_with_values[current_level]
#         altitude_names.popleft()
#         print(f"John has reached: {current_level}")
#     else:
#         fuel.pop()
#         consumption_index.popleft()
#         altitude_names.popleft()
#         print(f"John did not reach: {current_level}")
#         break
#
# # Output results
# if not altitudes_with_values:
#     print("John has reached all the altitudes and managed to reach the top!")
# else:
#     print("John failed to reach the top.")
#     if reached_altitudes:
#         print("Reached altitudes: ", end="")
#         print(", ".join(reached_altitudes))
#     else:
#         print("John didn't reach any altitude.")
