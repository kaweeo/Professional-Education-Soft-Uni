aninmal = input()
reptiles = ["crocodile", "tortoise", "snake"]
if aninmal == "dog":
    print("mammal")
elif aninmal in reptiles:
    print("reptile")
else:
    print("unknown")