
number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    reservation_code = input()
    reservations.add(reservation_code)

guest_incomming = input()
guests_that_came = set()
while guest_incomming != "END":
    guests_that_came.add(guest_incomming)
    guest_incomming = input()

guest_didnt_come = reservations.difference(guests_that_came)
guest_didnt_come_tuple = tuple(guest_didnt_come)
guest_didnt_come_list = sorted(guest_didnt_come_tuple)
print(len(guest_didnt_come_tuple))
for item in guest_didnt_come_list:
    print(item)