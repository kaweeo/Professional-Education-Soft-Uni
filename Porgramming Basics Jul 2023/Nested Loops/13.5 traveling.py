
flag = True
while flag == True:
    destination = input()
    if destination == "End":
        break
    min_budjet = float(input())
    tot_saved = 0
    while flag == True:
        saved_in = float(input())
        tot_saved += saved_in
        if tot_saved >= min_budjet:
            print(f"Going to {destination}!")
            break