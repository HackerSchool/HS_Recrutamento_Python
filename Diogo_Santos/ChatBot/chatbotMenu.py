from ChatBot.chatbot import Chatbot
from user import User

class ChatbotMenu:
    ''' The chatbot menu to be displayed when app is open

    Attributes:
        user         The user in app
        calculator   The chatbot core
        menuText    The menu text to be displayed
    '''

    def __init__(self,user: User,chatbot: Chatbot) -> None:
        ''' Creates an instance of the class ChatbotMenu '''
        self.user = user
        self.chatbot = chatbot
        self.menuText = '''\nChoose an option:
            1 - ZenBot
            2 - Exit App
            '''


    def menu(self) -> None:
        ''' Displays menu and waits for user input '''
        print(self.menuText)
        self.__options()


    def __options(self) -> None:
        ''' Receives and processes user input '''

        n = input("Option: ")
        
        if n == "1":
            self.ZenBot()
        elif n == "2":
            self.exitApp()
        else:
            print("Not an available option.")


    def ZenBot(self) -> None:
        ''' Starts a conversation with Zenbot'''
        self.chatbot.ZenBot()


    def exitApp(self) -> None:
        ''' Exits app '''
        self.user.exitApp()
