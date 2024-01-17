from collections import deque

number_of_stations = int(input())
circle_track = deque()
current_tank = 0
index = 0

for _ in range(number_of_stations):
    amount_of_petrol, distance_to_next_station = [int(input_element) for input_element in input().split(" ")]
    circle_track.append([amount_of_petrol, distance_to_next_station])

circle_track_copy = circle_track.copy()   # making a copy, to pop() elements, if element popped is not correct, \
                                          #      the copy will get the initial value

while circle_track_copy:
    amount_of_petrol, distance_to_next_station = circle_track_copy.popleft()

    current_tank += amount_of_petrol

    if current_tank >= distance_to_next_station:
        current_tank -= distance_to_next_station
    else:
        circle_track.rotate(-1)
        circle_track_copy = circle_track.copy()   # making a new copy, the old one has already items popped
        index += 1
        current_tank = 0

print(index)