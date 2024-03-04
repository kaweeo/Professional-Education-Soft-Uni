from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[object] = []
        self.books_available: Dict[str: List[str]] = {}  # {author: [available_book1, available_book2, ...]}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for values in self.rented_books.values():
            if book_name in values.keys():
                return f'The book "{book_name}" is already rented and will be available in {values[book_name]} days!'

        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books.keys():
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"


    ## 2nd version for return_book method, where checking in Library insted of User
    # def return_book(self, author: str, book_name: str, user: User) -> str:
    #     if book_name not in self.rented_books[user.username]:
    #         return f"{user.username} doesn't have this book in his/her records!"
    #
    #     del self.rented_books[user.username][book_name]
    #     user.books.remove(book_name)
    #     self.books_available[author].append(book_name)