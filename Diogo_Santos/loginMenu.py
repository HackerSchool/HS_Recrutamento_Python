from user import User
from database import *
from login import Login

class LoginMenu:
    '''The login menu to be displayed to not authenticated users

    Attributes:
        user        The user to be loggen in
        exitState   The intention of exiting the program
        loginApp    The login core
        menuText    The menu text to be displayed

    Functionality:
        Login
        Register
        Exit
    '''

    def __init__(self, user: User) -> None:
        """ Creates an instance of the class LoginMenu """
        self.user = user
        self.exitState = False
        self.loginApp = Login(user)
        self.menuText = '''\nChoose an option:
            1 - Register
            2 - Login
            3 - Exit
            '''

    def menu(self) -> None:
        """ Displays menu and waits for user input """
        print(self.menuText)
        self.__options()


    def __options(self) -> None:
        """ Receives and processes user input """

        n = input("Option: ")

        if n == "1":
            self.register()
        elif n == "2":
            self.login()
        elif n == "3":
            self.exit()
        else:
            print("Not an available option.")


    def login(self) -> None:
        """ Logins user """
        self.loginApp.login()
    

    def register(self) -> None:
        """ Logouts user """
        self.loginApp.register()


    def exit(self) -> None:
        """ Sets exitState to True """
        self.exitState = True