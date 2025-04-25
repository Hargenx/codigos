from model import Book
from view import View
from database import DatabaseConnection

class Controller:
    def __init__(self, db_type="sqlite"):
        self.view = View()
        self.db = DatabaseConnection(db_type)
        self.db.connect()
        self.db.create_table()

    def run(self):
        while True:
            option = self.view.show_menu()
            match option:
                case '1':
                    self.add_book()
                case '2':
                    self.list_books()
                case '3':
                    self.remove_book()
                case '4':
                    self.view.show_message("Exiting the program. Goodbye!")
                    self.db.close()
                    break
                case _:
                    self.view.show_message("Invalid option. Please try again.")
'''            if option == '1':
                self.add_book()
            elif option == '2':
                self.list_books()
            elif option == '3':
                self.remove_book()
            elif option == '4':
                self.view.show_message("Exiting the program. Goodbye!")
                self.db.close()
                break
            else:
                self.view.show_message("Invalid option. Please try again.")'''

    def add_book(self):
        title, author, year = self.view.get_book_info()
        self.db.insert_book(title, author, year)
        self.view.show_message("Book added successfully!")

    def list_books(self):
        books = self.db.fetch_books()
        self.view.show_books(books)

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.db.remove_book(title)
        self.view.show_message("Book removed (if it existed).")
