class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        if hasattr(self, 'file') and self.file is not None:
            self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        for line in lines:
            info = line.split(",")
            print(f"Book Name: {info[0]},  Author: {info[1]}")

    def add_book(self):
        name = input("Enter book name: ")
        author = input("Enter book author: ")
        release_date = input("Enter first release date: ")
        pages = input("Enter number of pages: ")
        book_info = f"{name},{author},{release_date},{pages}\n"
        self.file.write(book_info)

    def delete_book(self):
        del_name = input("Enter the name of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()

        books = []
        for line in lines:
            info = line.split(",")
            books.append(info)

        for book in books:
            if del_name in book:
                books.remove(book)
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(f"{book[0]},{book[1]},{book[2]},{book[3]}\n")


lib = Library()

while True:
    print("""
    1) List all books
    2) Add a book 
    3) Delete a book
    q) Quit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":

        lib.delete_book()
    elif choice == "q":
        print("Have a nice day!")
        break
    else:
        print("Invalid choice!")
