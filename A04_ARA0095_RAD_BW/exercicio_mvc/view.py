class View:
    def show_menu(self):
        print("\n=== Menu ===")
        print("1. Add book")
        print("2. List books")
        print("3. Remove book")
        print("4. Exit")
        return int(input("Choose an option: "))

    def get_book_info(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the year of publication: ")
        return title, author, int(year)

    def show_books(self, books):
        if not books:
            print("No books registered.")
        else:
            print("\n=== Book List ===")
            for book in books:
                print(book)

    def show_message(self, message):
        print(message)
