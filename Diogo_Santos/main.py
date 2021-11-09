from loginMenu import LoginMenu
from appMenu import AppMenu
from user import User

'''
A brief explanation:
The core philosophy of this program is to divide each App in two parts:
    The Menu - responsible for the looks and logic of the menu
    The App - responsible for the implementation of all functionally

Some improvements for the future in the bottom.
'''


if __name__ == "__main__":

    user = User()
    loginMenu = LoginMenu(user)
    appMenu = AppMenu(user)
    
    # Main Menu Logic
    while True:

        if(loginMenu.exitState == True):
            break

        if(user.loggedIn):
            if(user.inApp):
                if(user.currentApp == "tictactoe"):
                    appMenu.tictactoeMenu()
                elif(user.currentApp == "chatbot"):
                    appMenu.chatbotMenu()
                elif(user.currentApp == "calculator"):
                    appMenu.calculatorMenu()
            else:
                appMenu.menu()
        else:
            loginMenu.menu()


'''
A superclass App to join the "menu" and "app" entities.
A superclass Menu would prevent code repetitions, more specifically the
menu() and __options() methods, having a generic method which receives
functions as parameters may be a solution.
'''