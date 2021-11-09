import matplotlib.pyplot as plt
import numpy as np
from user import User

class Calculator:
    ''' The core of the app tictactoe

    Attributes:
        user            The user in app
    
    This app allows the user to calculate algebraic expressions with one operation,
    to calculate the sum/sub/mult of two matrixes and to graph a polynomial function.
    '''

    def __init__(self, user: User) -> None:
        ''' Creates an instance of the class Calculator '''
        self.user = user


    def oneOperationSolver(self) -> None:
        ''' Solves an algebraic expression with one operation '''
        
        expression = input("Expression: ").replace(" ","")
        try:
            res = self.__expressionComputation(expression)
        except Exception:
            print("Could not compute expression")
            return
        if(res == None):
            print("Error computing expression")
            return 
        print(f"Result: {res}")
   
    
    def __expressionComputation(self, expression: str) -> float:
        ''' Parses and calculates the user given expression '''
        operations = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "x": lambda x,y: x * y,
            "/": lambda x,y: x / y,
            "**":lambda x,y: x ** y,
            "%": lambda x,y: x % y
        }

        # Deals with expressions that start with -
        k = 1
        if(expression[0] == "-"):
            k = -1
            expression = expression[1:]

        for operation in operations:
            if(len(expression.split(operation))>1):
                num1,num2 = expression.split(operation)
                return operations[operation](k*float(num1),float(num2))


    def matrixOperation(self) -> None:
        ''' Solves a matrix algebraic expression with one operation '''

        dim1 = input("Dimensions of first matrix.\nEx: 2x3\nDimensions: ").split("x")
        dim2 = input("Dimensions of second matrix.\nEx: 3x1\nDimensions: ").split("x")

        try:
            n1,m1 = int(dim1[0]),int(dim1[1])
            n2,m2 = int(dim2[0]),int(dim2[1])
        except Exception:
            print("Could not compute matrix dimensions")
            return

        matrix1 = [[None for _ in range(m1)] for _ in range(n1)]
        matrix2 = [[None for _ in range(m2)] for _ in range(n2)]

        try:
            print("Enter first matrix line by line.\nEx: 1 2 3 ENTER 2 3 1")
            self.__fillMatrixFromInput(n1,m1,matrix1)

            print("Enter second matrix line by line.\nEx: 1 ENTER 2 ENTER 1")
            self.__fillMatrixFromInput(n2,m2,matrix2)
        except Exception:
            print("Could not compute matrix values")

        operation = input("Choose an operation, available: +/-/*\nOperation: ")

        if operation == "+":
            result = self.__sumMatrixes(n1,m1,matrix1,n2,m2,matrix2)
        elif operation == "-":
            result = self.__subtractMatrixes(n1,m1,matrix1,n2,m2,matrix2)
        elif operation == "*":
            result = self.__multiplyMatrixes(n1,m1,matrix1,n2,m2,matrix2)
        else:
            print("Not supported operation")
            return

        print(f"Here is the result:\n{result}")
  
    
    def __sumMatrixes(self, n1: int, m1: int, matrix1: list, n2: int, m2: int, matrix2: list) -> int:
        ''' Sums two matrixes '''

        result = [[None for x in range(m1)] for y in range(n1)]
        
        #Verify is matrixes have correct dimmensions to be summed
        if(n1 != n2 or m1 != m2):
            print("Can't sum matrixes with different dimensions")
        
        for i in range(n1):
            for j in range(m1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]

        return result


    def __subtractMatrixes(self, n1: int, m1: int, matrix1: list, n2: int, m2: int, matrix2: list) -> int:
        ''' Subtracts two matrixes '''

        result = [[None for x in range(m1)] for y in range(n1)]
        
        #Verify is matrixes have correct dimmensions to be subtracted
        if(n1 != n2 or m1 != m2):
            print("Can't subtract matrixes with different dimensions")
            return
        
        for i in range(n1):
            for j in range(m1):
                result[i][j] = matrix1[i][j] - matrix2[i][j]

        return result


    def __multiplyMatrixes(self, n1: int, m1: int, matrix1: list, n2: int, m2: int, matrix2: list) -> int:
        ''' Multiplies two matrixes '''

        def getColumn(n,k,matrix):
            result = []
            for i in range(n):
                result.append(matrix[i][k])
            return result

        result = [[None for x in range(m2)] for y in range(n1)]
        
        #Verify is matrixes have correct dimmensions to be subtracted
        if(m1 != n2):
            print("Can't multiply matrixes in which the number of columns in the first matrix isn't equal to the number of rows in the second matrix")
            return

        for i in range(n1):
            for j in range(m2):
                line = matrix1[i]
                column = getColumn(n2,j,matrix2)
                result[i][j] = sum([x*y for x,y in zip(line,column)])

        return result
        

    def __fillMatrixFromInput(self, n:int, m:int, matrix: list):
        ''' Fills matrixes with user inputs '''

        for i  in range(n):
            line = input("Elements: ").split(" ")
            if(len(line) != m):
                print("Incorrect number of elements")
                return
            for j in range(m):
                matrix[i][j] = int(line[j])

        

    def graphFunction(self) -> None:
        ''' Plots a graph for a polynomial function '''
        
        print("\nPlot a polynomial function\nEx: 3x^2+x+2")

        func = input("Function: ")
        try:
            x,y = self.__parsePolynomialFunction(func)
        except Exception:
            print("Could not compute function")
            return
        plt.plot(x,y)
        plt.grid(True)
        plt.show()


    def __parsePolynomialFunction(self, func: str) -> np.linspace:
        ''' Parses the user given polynomial '''

        funcToSplit = func[0] + func[1:].replace("-","+-")
        funcSplitted = funcToSplit.split("+")

        funcCoefPow = []
        for element in funcSplitted:
            pair = self.__parseElement(element)
            funcCoefPow.append(pair)

        # Create 21 values from -10 to 10
        x = np.linspace(-10,10,21)
        y = 0
        for pair in funcCoefPow:
            y += pair[0]*(x**pair[1])

        return x,y


    def __parseElement(self, element: str) -> tuple:
        ''' Parses single element of type ax^b '''

        # For general case ax^b any a,b
        if(element.find("x^") != -1):
            elementPart1, elementPart2 = element.split("x^")

            # General case ax^b
            if(len(elementPart1) != 0):
                elementCoef = self.__parseElementPart(elementPart1)
            # Case for x^b
            else:
                elementCoef = 1
            
            # Length must be >0 because ax^ doest make sense
            elementPow = self.__parseElementPart(elementPart2)

        # For ax case
        elif(element.find("x") != -1):
            elementPart1, _ = element.split("x")

            # General case ax
            if(len(elementPart1) != 0):
                elementCoef = self.__parseElementPart(elementPart1)
            # Case for x
            else:
                elementCoef = 1

            elementPow = 1

        # For a case
        else:
            elementCoef = int(element)
            elementPow = 0

        return (elementCoef, elementPow)

    
    def __parseElementPart(self, elementPart: str) -> int:
        ''' Parses specific element of type ax '''

        if(len(elementPart) == 1 and elementPart[0] == "-"):
            number = -1
        else:
            number = int(elementPart)

        return number