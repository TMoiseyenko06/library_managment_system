class Book():
    def __init__(self,name,author,borrowed=False,user=None):
        self.__name = name
        self.__borrowed = borrowed
        self.__user = user
        self.__author = author

    def get_name(self):
        return self.__name
    
    def get_user(self):
        return self.__user

    def borrow_book(self,user):
        if self.__borrowed == False:
            self.__borrowed = True
            self.__user = user
            print(f'The Book {self.__name} has been borrowed by {self.__user}!')
        else:
            print(f'The user {self.__user} already has this book!')

    def return_book(self,user):
        if not self.__user == user:
            print(f'User {user} is not able to return this book because he does not have it!')
        else:
            self.__user = None
            self.__borrowed = False
            print(f'{user} has succsesfully returned {self.__name}')   

    def print_book_data(self):
        print(f'Book Title: {self.__name}, {'Avalible' if self.__borrowed == False else f'Currently being borrowed by {self.__user}'}')

class Author():
    def __init__(self,name,bio):
        self.__name = name
        self.__bio = bio

    def get_details(self):
        print(f'{self.__name}:\n{self.__bio}')

    def get_name(self):
        return self.__name

class User():

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name




