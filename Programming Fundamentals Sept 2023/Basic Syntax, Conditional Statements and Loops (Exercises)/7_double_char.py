
flag = False

while flag == False:
    string = input()
    if string == "End":
        flag == True
        break
    if string == "SoftUni":
        continue
    doubled_string = ""
    for char in string:
        doubled_string += char * 2
    print(doubled_string)
