
version = input()
version_list = version.split(".")
version_list = [int(s) for s in version_list]
version_list[2] += 1
if version_list[2] == 10:
    version_list[2] = 0
    version_list[1] += 1
    if version_list[1] == 10:
        version_list[1] = 0
        version_list[0] += 1
result = '.'.join(str(item) for item in version_list)
print(result)