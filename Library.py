class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id  
        self.__title = title      
        self.__author = author    
        self.__availability = True  

        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You have successfully borrowed the book: {self.__title}")
        else:
            print(f"The book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have successfully returned the book: {self.__title}")
        else:
            print(f"The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Borrowed"
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\nAuthor: {self.__author}\nAvailability: {availability_status}\n")

    def get_book_id(self):
        return self.__book_id

def main_menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if not Library.book_list:
                    print("No books are available in the library.")
                else:
                    print("\nAvailable Books:")
                    for book in Library.book_list:
                        book.view_book_info()

            elif choice == 2:
                book_id = input("Enter the Book ID to borrow: ")
                for book in Library.book_list:
                    if book.get_book_id() == book_id:
                        book.borrow_book()
                        break
                else:
                    print("Invalid Book ID.")

            elif choice == 3:
                book_id = input("Enter the Book ID to return: ")
                for book in Library.book_list:
                    if book.get_book_id() == book_id:
                        book.return_book()
                        break
                else:
                    print("Invalid Book ID.")

            elif choice == 4:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please choose a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

book1 = Book("101", "The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("102", "To Kill a Mockingbird", "Harper Lee")
book3 = Book("103", "1984", "George Orwell")

main_menu()

