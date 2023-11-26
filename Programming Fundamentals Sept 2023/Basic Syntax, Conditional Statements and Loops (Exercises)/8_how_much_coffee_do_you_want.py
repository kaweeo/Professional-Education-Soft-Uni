coffees = 0
commands = ["coding", "movie", "dog", "cat"]
flag = False
while True:
    command = input()
    if command == "END":
        if coffees > 5:
            break
        else:
            print(f"{coffees}")
            break
    if command in commands:
        coffees += 1
    elif command.lower() in commands:
        coffees += 2
    if coffees == 5 and flag == False:
        print("You need extra sleep")
        flag = True
    elif coffees == 5 and flag == True:
        pass

    # -----------------

coffee_counter = 0
command = input()

while command != "END":
    if command.lower() == "coding" \
           or command.lower() == "dog" \
           or command.lower() == "cat" \
           or command.lower() == "movie":
         if command.islower():
              coffee_counter += 1
         else:
              coffee_counter += 2

    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)