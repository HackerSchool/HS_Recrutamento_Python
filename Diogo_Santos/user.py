class User:
    '''The user entity

    Attributes:
        name        The username by which the user is referenced to
        loggenIn    The state that tracks if user is loggen in
        inApp       The state that tracks if user is in an app
        currentApp  The name of the app the user is currently in

    Notice that during runtime the program only has one instance of "User"
    this can be seen as a singleton which tracks which user is currently
    loggen in.

    Could be further expanded and stored in a DB with personal information 
    (e.g. games lost against AI in TicTacToe).
    '''
    def __init__(self) -> None:
        """ Creates an instance of the class User """
        self.name = ""
        self.loggedIn = False
        self.inApp = False
        self.currentApp = ""

    def getName(self) -> str:
        """ Returns the user name """
        return self.name

    def login(self, username: str) -> None:
        """ Logs user """
        self.name = username
        self.loggedIn = True

    def logout(self) -> None:
        """ Logs out user """
        self.name = ""
        self.loggedIn = False

    def enterApp(self, app: str) -> None:
        """ Updates inApp status """
        self.inApp = True
        self.currentApp = app

    def exitApp(self) -> None:
        """ Updates inApp status """
        self.inApp = False
        self.currentApp = ""