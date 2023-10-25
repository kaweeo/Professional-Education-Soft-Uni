hours = int(input())
mins = int(input())

mins += 15
if mins > 59:
    hours +=1
    mins = mins - 60
if mins < 10:
    mins = str(f"0{mins}")
if hours == 24:
    hours = 00
print(f"{hours}:{mins}")
