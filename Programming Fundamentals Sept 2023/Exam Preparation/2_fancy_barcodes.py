import re

n = int(input())

pattern = r'@#+(\b[A-Z][A-Za-z0-9]{4,}[A-Z]\b)@#+'

for input_barcode in range(n):
    input_barcode = input()
    match = re.search(pattern, input_barcode)
    if match:
        barcode = match.group(1)
        product_group = ""
        for symbol in barcode:
            if symbol.isdigit():
                product_group += symbol
        if product_group == "":
            print(f"Product group: 00")
        else:
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")