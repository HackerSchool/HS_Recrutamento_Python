from user import User
from database import *

class Login:
    """ The core of login

    Attributes:
        user        The user in app
    """
    def __init__(self, user: User) -> None:
        """ Creates an instance of the class Login """
        self.user = user


    def login(self) -> None:
        """ Displays login form and proccess it """

        print("\n---Login Form---")

        userName = input("Name: ")
        userPassword = input("Password: ")

        # Check credentials
        if(checkCorrectCredentials(userName,userPassword)):
            self.user.login(userName)
            print("---Login Successful---")
        else:
            print("---Login Fail---")


    def register(self) -> None:
        """ Displays register form and proccess it """

        print("\n---Register Form---")

        # Checks name
        userName = input("Name: ")
        while(checkNameExists(userName)):
            print("Username already taken.")
            userName = input("Name: ") 

        # Checks password strength
        userPassword = input("Password: ")
        while(checkStrengthPassword(userPassword) < 5):
            print("Password too weak.")
            print("Try using digits or lower/upper case letters")
            userPassword = input("Password: ")

        # Add to database
        addNewUser(userName,userPassword)

        print("---Register successful---")
