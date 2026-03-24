# Library system using Book, Member, Library classes with menu-driven operations

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added!")

    def add_member(self, name):
        self.members.append(Member(name))
        print("Member added!")

    def lend_book(self, title, member_name):
        for book in self.books:
            if book.title == title and book.available:
                for member in self.members:
                    if member.name == member_name:
                        book.available = False
                        member.borrowed_books.append(title)
                        print("Book lent successfully!")
                        return
        print("Book not available or member not found!")

    def return_book(self, title, member_name):
        for member in self.members:
            if member.name == member_name and title in member.borrowed_books:
                member.borrowed_books.remove(title)
                for book in self.books:
                    if book.title == title:
                        book.available = True
                print("Book returned!")
                return
        print("Return failed!")

    def display_books(self):
        print("\n--- Books ---")
        for book in self.books:
            status = "Available" if book.available else "Lent"
            print(f"{book.title} - {status}")


def menu():
    lib = Library()

    while True:
        print("\n1.Add Book 2.Add Member 3.Lend Book 4.Return Book 5.Display Books 6.Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            lib.add_book(input("Book title: "))
        elif choice == '2':
            lib.add_member(input("Member name: "))
        elif choice == '3':
            lib.lend_book(input("Book title: "), input("Member name: "))
        elif choice == '4':
            lib.return_book(input("Book title: "), input("Member name: "))
        elif choice == '5':
            lib.display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
