import os
import random
from abc import ABC, abstractmethod
from tictactoe import TicTacToe
from calculator import Calculator

class AuthenticationSystem(ABC):

    # returns true if the user exists
    @abstractmethod
    def user_exists(self, username):
        pass

    # registers a new user
    # returns False if that username is in use
    @abstractmethod
    def register_user(self, username, password):
        pass

    # updates an already existing user credentials
    @abstractmethod
    def update_user_credentials(self, username, new_password):
        pass

    # returns True if the provided credentials match any of the existing ones
    # returns false otherwise
    @abstractmethod
    def login_user(self, user, password):
        pass


# stores username and password combos in plain text in a file named in the constructor
# DO NOT USE FOR ANYTHING EVER!!!!
class InsecureAuthenticationSystem(AuthenticationSystem):

    # takes the name of the file, creates said file if it doesn't exist
    def __init__(self, credentials_file):
        self.__credentials_file = credentials_file
        self.__user_credentials_dict = {}
        if not os.path.exists(f"./{self.__credentials_file}"):
            open(self.__credentials_file, "w").close()
        self.__credentials_load()

    # loads credentials from the file to the dictionary
    def __credentials_load(self):
        credentials = open(self.__credentials_file)
        for line in credentials:
            user, password = line.strip().split(" : ")
            self.__user_credentials_dict[user] = password
        credentials.close()

    # writes the full dictionary overwriting the file
    def __credentials_store(self):
        credentials = open(self.__credentials_file, 'w')
        for user in self.__user_credentials_dict.keys():
            credentials.write(f"{user} : {self.__user_credentials_dict[user]}\n")
        credentials.close()

    def __user_password(self, user):
        return self.__user_credentials_dict[user]

    def user_exists(self, username):
        return username in self.__user_credentials_dict

    def register_user(self, username, password):
        if self.user_exists(username):
            return False
        self.__user_credentials_dict[username] = password
        self.__credentials_store()
        return True

    def update_user_credentials(self, username, new_password):
        self.__user_credentials_dict[username] = new_password
        self.__credentials_store()

    def login_user(self, user, password):
        if self.user_exists(user):
            if password == self.__user_password(user):
                return True
        return False


class HackerschoolApp:

    def __init__(self):
        self.auth_system = InsecureAuthenticationSystem("user_credentials.txt")

    def page_main_menu(self):
        page = "Welcome To HackerSchool\n" + \
               "Please pick one of the following options\n" + \
               "l: Login\n" + \
               "r: Register\n" + \
               "q: Quit Program\n"

        while True:
            self.page_clear()
            print(page)
            user_choice = input(">")
            if user_choice == "q":
                return
            if user_choice == "r":
                self.page_register()
            if user_choice == "l":
                self.page_login()

    def page_register(self):
        self.page_clear()
        while True:
            print("Please insert the desired username\n")
            username = input("username>")
            print("Please insert the desired password\n")
            password = input("password>")
            if self.auth_system.register_user(username, password):
                self.page_clear()
                print("New Account Registered Successfully\n")
                input("Press ENTER to go back to the main page")
                break
            else:
                print("User Already Exists\n")
                while True:
                    user_choice = input("Retry(r)or Quit(q)")
                    if user_choice == "q":
                        return
                    elif user_choice == "r":
                        break

    def page_login(self):
        while True:
            self.page_clear()
            username = input("username>")
            password = input("\npassword>")
            if self.auth_system.login_user(username, password):
                self.page_authenticated_menu(username)
                break
            else:
                self.page_clear()
                print("Login Failed\n")
                while True:
                    user_choice = input("Retry(r)or Quit(q)")
                    if user_choice == "q":
                        return
                    elif user_choice == "r":
                        break

    def page_authenticated_menu(self, username):
        self.page_clear()
        page = f"Welcome {username}!!!\n" + \
               "Please pick one of the following options\n" + \
               "t: To Play TicTacToe\n" + \
               "m: To Open the Calculator\n" +\
               "c: Change Password\n" +\
               "l: Logout\n"
        while True:
            self.page_clear()
            print(page)
            user_choice = input(">")
            if user_choice == "l":
                return
            elif user_choice == "m":
                self.page_clear()
                Calculator().run()
            elif user_choice == "c":
                self.page_change_credentials(username)
            elif user_choice == "t":
                TicTacToe().menu()

    def page_change_credentials(self, username):
        self.page_clear()
        print(f"Please insert a new password for {username}\n")
        new_password = input(">")
        self.auth_system.update_user_credentials(username, new_password)
        print("password updated successfully please press ENTER to go back\n")
        input()

    @staticmethod
    def page_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


random.seed()
app = HackerschoolApp()
app.page_main_menu()
