#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_by = []

    def is_available(self):
        return self.copies > len(self.borrowed_by)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available():
                print(f"Title: {book.title}, Author: {book.author}, Copies available: {book.copies - len(book.borrowed_by)}")

    def borrow_book(self, title, borrower):
        for book in self.books:
            if book.title == title and book.is_available():
                book.borrowed_by.append(borrower)
                print(f"{borrower} has borrowed '{book.title}'. Enjoy reading!")
                return
        print("Book not found in the library or currently not available.")

    def return_book(self, title, borrower):
        for book in self.books:
            if book.title == title and borrower in book.borrowed_by:
                book.borrowed_by.remove(borrower)
                print(f"Thank you, {borrower}, for returning '{book.title}'.")
                return
        print("Book not found in the library or not borrowed by the specified borrower.")

# Sample usage
if __name__ == "__main__":
    library = Library()
    book1 = Book("Harry Potter", "J.K. Rowling", 5)
    book2 = Book("Lord of the Rings", "J.R.R. Tolkien", 3)
    library.add_book(book1)
    library.add_book(book2)

    print("Welcome to the Library Management System!")
    while True:
        print("\nMenu:")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            borrower = input("Enter your name: ")
            library.borrow_book(title, borrower)
        elif choice == "3":
            title = input("Enter the title of the book you want to return: ")
            borrower = input("Enter your name: ")
            library.return_book(title, borrower)
        elif choice == "4":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


# 
