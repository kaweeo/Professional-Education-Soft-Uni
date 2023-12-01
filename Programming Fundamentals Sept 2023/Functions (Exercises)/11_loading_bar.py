n = int(input())
loaded_procents = ""
left_to_load = int(10 - n / 10)
dots = left_to_load * "."
loaded = (10 - left_to_load) * 10

for n in range (1, n + 1, 10):
    loaded_procents += "%"

if left_to_load == 0:
    print("100% Complete!")
    print(f"[{loaded_procents + dots}]")
else:
    print(f"{loaded}% [{loaded_procents + dots}]")
    print("Still loading...")

