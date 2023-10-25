paper_price = 5.8
cotton_price = 7.2
glue_price = 1.2

paper_count = int(input())
cotton_count = int(input())
glue_count = float(input())
discount = int(input())

total = paper_price * paper_count + cotton_count * cotton_price + glue_count * glue_price
total_with_discount = total - total * (discount / 100)
print(f"{total_with_discount:.3f}")