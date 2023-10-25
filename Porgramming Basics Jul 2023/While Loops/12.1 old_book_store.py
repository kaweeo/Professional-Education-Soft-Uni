ani_s_book = input()
book_counter = 0

while True:
    searched_book = input()
    book_counter += 1
    if searched_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter - 1} books.")
        break
    elif searched_book == ani_s_book:
        print(f"You checked {book_counter - 1} books and found it.")
        break