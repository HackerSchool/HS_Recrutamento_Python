from Calculator.calculator import Calculator
from Calculator.calculatorMenu import CalculatorMenu
from ChatBot.chatbot import Chatbot
from ChatBot.chatbotMenu import ChatbotMenu
from TicTacToe.tictactoe import Tictactoe
from TicTacToe.tictactoeMenu import TicTacToeMenu
from user import User
from database import *

class AppMenu:
    '''The menu displayed to authenticated in users

    Attributes:
        user            The loggen in user
        tictactoeApp    The tictactoe app 
        calculatorApp   The calculator app 
        chatbotApp      The chatbot app 
        menuText       The menu text to be displayed

    Functionally:
        Open tictactoe
        Open calculator
        Open chatbot
        Change password
        Loggout
    '''

    def __init__(self, user: User) -> None:
        """ Creates an instance of the class AppMenu """
        self.user = user
        self.tictactoeApp = TicTacToeMenu(self.user,Tictactoe(self.user))
        self.calculatorApp = CalculatorMenu(self.user,Calculator(self.user))
        self.chatbotApp = ChatbotMenu(self.user,Chatbot(self.user))
        self.menuText = '''\nChoose an option:
            1 - TicTacToe
            2 - Calculator
            3 - Chatbot
            4 - Change password
            5 - Logout
            '''


    def menu(self) -> None:
        """ Displays menu and waits for user input """
        print(self.menuText)
        self.__options()


    def __options(self) -> None:
        """ Receives and processes user input """

        n = input("Option: ")
        
        if n == "1":
            self.tictactoeMenu()
        elif n == "2":
            self.calculatorMenu()
        elif n == "3":
            self.chatbotMenu()
        elif n == "4":
            self.changePassword()
        elif n == "5":
            self.logout()
        else:
            print("Not an available option.")


    def tictactoeMenu(self) -> None:
        """ Opens tictactoe app and sets current app in User """
        self.user.enterApp("tictactoe")
        self.tictactoeApp.menu()

    
    def calculatorMenu(self) -> None:
        """ Opens calculator app and sets current app in User """
        self.user.enterApp("calculator")
        self.calculatorApp.menu()


    def chatbotMenu(self) -> None:
        """ Opens chatbot app and sets current app in User """
        self.user.enterApp("chatbot")
        self.chatbotApp.menu()


    def changePassword(self) -> None:
        """ Changes user password """

        userName = self.user.getName()

        attempts = 0
        # Verify user
        oldPassword = input("Old Password: ")
        while(not checkCorrectPassword(userName, oldPassword)):
            # Repeated attempts
            if(attempts == 3):
                print("Too many attempts.")
                break
            attempts += 1
            print("Wrong Password")
            oldPassword = input("Old Password: ")
        
        # New password
        newPassword = input("New Password: ")
        while(checkStrengthPassword(newPassword) < 5):
            print("Password too weak.")
            newPassword = input("New Password: ")

        # Change database
        changePassword(userName, newPassword)
        print("New Password Set.")


    def logout(self) -> None:
        """ Logouts user """
        self.user.logout()