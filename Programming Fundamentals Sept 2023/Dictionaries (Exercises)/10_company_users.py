
company_data = {}

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" -> ")
    company_name = command[0]
    employee_id = command[1]

    if not company_name in company_data.keys():
        company_data[company_name] = [employee_id]
    else:
        if employee_id not in company_data[company_name]:
            company_data[company_name].append(employee_id)

for k, v in company_data.items():
    print(f"{k}")
    for employee in v:
        print(f"-- {employee}")

