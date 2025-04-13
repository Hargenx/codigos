from model import Book
from view import View
class Controller:
    def __init__(self) -> None:
        self.books = []
        self.view = View()

    def run(self):
        while True:
            option = self.view.show_menu()
            match option:
                case 1:
                    self.add_book()
                case 2:
                    self.list_books()
                case 3:
                    self.remove_book()
                case 4:
                    self.view.show_message("Exiting...\n\t Goodbye! \n\tMate!")
                    break
                case _:
                    self.view.show_message("Invalid option. Please try again.")
                    continue


    def add_book(self):
        title, author, year = self.view.get_book_info()
        book = Book(title, author, year)
        self.books.append(book)
        self.view.show_message("Book added successfully!")

    def list_books(self):
        self.view.show_books(self.books)

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.view.show_message("Book removed successfully!")
                return
        self.view.show_message("Book not found.")