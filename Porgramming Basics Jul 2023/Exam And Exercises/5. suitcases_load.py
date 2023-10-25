
capacity = float(input())
total_luggage = 0
suitcase_counter = 0

flag = True
while flag:
    end_or_suitcase = input()
    if end_or_suitcase == "End":
        print("Congratulations! All suitcases are loaded!")
        flag = False
        break
    suitcase = float(end_or_suitcase)
    total_luggage += suitcase
    if total_luggage >= capacity:
        print("No more space!")
        break
    suitcase_counter += 1

print(f"Statistic: {suitcase_counter} suitcases loaded.")