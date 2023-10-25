day = input()
working = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if day in working:
    print("Working day")
elif day in weekend:
    print("Weekend")
else:
    print("Error")