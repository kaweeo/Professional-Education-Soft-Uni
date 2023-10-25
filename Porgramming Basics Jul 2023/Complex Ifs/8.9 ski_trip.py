days_count = int(input())
room_type = input()
review_score = input()

nights = days_count - 1

if room_type == "room for one person":
    total = nights * 18
elif room_type == "apartment":
    if days_count < 10:
          total = nights * 25 * 0.7
    elif 10 <= days_count < 15:
          total = nights * 25 * 0.65
    elif days_count > 15:
          total = nights * 25 * 0.5
elif room_type == "president apartment":
    if days_count < 10:
        total = nights * 35 * 0.9
    elif 10 <= days_count < 15:
        total = nights * 35 * 0.85
    elif days_count > 15:
        total = nights * 35 * 0.8

if review_score == "positive":
    total_after_review = total * 1.25
else:
    total_after_review = total * 0.9

print(f"{total_after_review:.2f}")