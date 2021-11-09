from user import User
from Calculator.calculator import Calculator

class CalculatorMenu:
    ''' The calculator menu to be displayed when app is open

    Attributes:
        user            The user in app
        calculator      The calculator core
        menuText        The menu text to be displayed
    '''

    def __init__(self,user: User,calculator: Calculator) -> None:
        ''' Creates an instance of the class CalculatorMenu '''
        self.user = user
        self.calculator = calculator
        self.menuText = '''\nChoose an option:
            1 - One operation solver
            2 - Matrix Operations
            3 - Graph function
            4 - Exit App
            '''


    def menu(self) -> None:
        ''' Displays menu and waits for user input '''
        print(self.menuText)
        self.__options()


    def __options(self) -> None:
        ''' Receives and processes user input '''

        n = input("Option: ")
        
        if n == "1":
            self.oneOperationSolver()
        elif n == "2":
            self.matrixOperation()
        elif n == "3":
            self.graphFunction()
        elif n == "4":
            self.exitApp()
        else:
            print("Not an available option.")

    
    def oneOperationSolver(self) -> None:
        ''' Solves an algebraic expression with one operation '''
        self.calculator.oneOperationSolver()


    def matrixOperation(self) -> None:
        ''' Solves a matrix algebraic expression with one operation '''
        self.calculator.matrixOperation()


    def graphFunction(self) -> None:
        ''' Plots a graph for a polynomial function '''
        self.calculator.graphFunction()


    def exitApp(self) -> None:
        ''' Exits app '''
        self.user.exitApp()