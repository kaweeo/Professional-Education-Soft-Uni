month = input()  # May, June, July, August, September, October
nights_count = int(input())


if month == "May" or month == "October":
    studio_total = nights_count * 50
    apartment_total = nights_count * 65
    if 7 < nights_count < 14:
        studio_total = studio_total * 0.95
    elif nights_count > 14:
        studio_total = studio_total * 0.7
elif month == "June" or month == "September":
    studio_total = nights_count * 75.2
    apartment_total = nights_count * 68.7
    if nights_count > 14:
        studio_total = studio_total * 0.8
elif month == "July" or month == "August":
    studio_total = nights_count * 76
    apartment_total = nights_count * 77

if nights_count > 14:
    apartment_total = apartment_total * 0.9

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")