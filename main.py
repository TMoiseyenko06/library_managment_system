import managment as manage
import user_interface as UI

class Library(UI.UserInterface):
    def __init__(self,admin):
        self.__admin = admin
        self.__library = UI.UserInterface()
        self.__books = []
        self.__authors = []
        self.__users = []

    def run_library(self):
        print(f"Welcome {self.__admin}")
        while True:
            operation = self.__library.main_menu()
            if operation == 1:
                operation = self.__library.book_menu()
                if operation == 1:
                    self.__books.append(manage.Book(input('What is the name of this book?'),input('Who is the author of this book?')))
                elif operation == 2:
                    book = input('What is the name of the book you would like to borrow?')
                    user = input("Who is going to be borrowing this book?")
                    found = False
                    for item in self.__books:
                        if item.get_name() == book and user in [user.get_name() for user in self.__users]:
                            found = True
                            item.borrow_book(user)
                            break
                    if not found:
                        print(f'{'User' if not user in [user.get_name() for user in self.__users] else 'Book'} Not found, please try again.')                    
                elif operation == 3:
                    book = input('What is the name of the book you would like to return?')
                    user = input("Who is going to be returning this book?")
                    found = False
                    for item in self.__books:
                        if item.get_name() == book:
                            found = True
                            item.return_book(user)
                            break
                    if not found:
                        print('Book not found please try again!')     
                elif operation == 4:
                    book = input('What is the name of the book you would like to search for?')
                    found = False
                    for item in self.__books:
                        if item.get_name() == book:
                            found = True
                            item.print_book_data()
                            break
                    if not found: 
                        print('Book not found please try again.')
                else:
                    for item in self.__books:
                        item.print_book_data()
            elif operation == 2:
                operation = self.__library.user_menu()
                if operation == 1:
                    name = input('What is the name of the new user?')
                    self.__users.append(manage.User(name))
                    print(f'New user {name} has been created')
                elif operation == 2:
                    name = input('Whos details would you like to see?')
                    found = False
                    for item in self.__users:
                        found = True
                        if item.get_name() == name:
                            print(f"Here are {name}'s Current books!")
                            for book in self.__books:
                                if book.get_user() == name:
                                    book.print_book_data()
                else:
                    for user in self.__users:
                        print(f"{user.get_name()}'s Current Books:")
                        for book in self.__books:
                            if book.get_user() == user.get_name():
                                book.print_book_data()
            elif operation == 3:
                operation = self.__library.author_menu()
                if operation == 1:
                    self.__authors.append(manage.Author(input('What is the name of the author?'),input('What is their biography?')))
                elif operation == 2:
                    name = input('What author would you like to see the details of?')
                    for author in self.__authors:
                        if author.get_name() == name:
                            author.get_details()
                else:
                    for author in self.__authors:
                        author.get_details()
            else:
                break

main = Library('Coding Temple')
main.run_library()
            
