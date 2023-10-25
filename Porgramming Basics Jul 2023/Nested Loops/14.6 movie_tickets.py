movie_or_stop = input()
free_seats = int(input())
total_tickets = 0

while movie_or_stop != "Finish":
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    for seat in (1, free_seats + 1):
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "student":
            student_tickets += 1
            total_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            total_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            total_tickets += 1
    seats_sold_pro = total_tickets / free_seats * 100
    print(f"{movie_or_stop} - {seats_sold_pro}% full.")
    if movie_or_stop == "Finish":
        break
    movie_or_stop = input()

student_tickets_pro = student_tickets / total_tickets * 100
standard_tickets_pro = standard_tickets / total_tickets * 100
kids_tickets_pro = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_pro}% student tickets.")
print(f"{standard_tickets_pro}% standard tickets.")
print(f"{kids_tickets_pro}% kids tickets.")