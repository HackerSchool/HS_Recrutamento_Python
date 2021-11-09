from user import User
from TicTacToe.tictactoe import Tictactoe

class TicTacToeMenu:
    ''' The tictactoe menu to be displayed when app is open

    Attributes:
        user            The user in app
        tictactoe       The tictactoe core
        menuText        The menu text to be displayed
    '''

    def __init__(self,user: User,tictactoe: Tictactoe) -> None:
        ''' Creates an instance of the class TictactoeMenu '''
        self.user = user
        self.tictactoe = tictactoe
        self.menuText = '''\nChoose an option:
            1 - TicTacToe against Minimax AI
            2 - TicTacToe against Random AI
            3 - Exit App
            '''

    def menu(self) -> None:
        ''' Displays menu and waits for user input '''
        print(self.menuText)
        self.__options()


    def __options(self) -> None:
        ''' Receives and processes user input '''

        n = input("Option: ")
        
        if n == "1":
            self.tictactoeSmart()
        elif n == "2":
            self.tictactoeRandom()
        elif n == "3":
            self.exitApp()
        else:
            print("Not an available option.")


    def tictactoeSmart(self) -> None:
        ''' Starts a game of tictactoe with smart AI '''
        self.tictactoe.startGame(smart=True)

    def tictactoeRandom(self) -> None:
        ''' Starts a game of tictactoe with random AI '''
        self.tictactoe.startGame(smart=False)

    def exitApp(self) -> None:
        ''' Exits app '''
        self.user.exitApp()
