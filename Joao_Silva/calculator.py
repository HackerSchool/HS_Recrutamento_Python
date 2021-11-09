#Operations---------------------------------------------------------------------
#Unique unary operations
def doOperation(v1, v2, operation):
    if operation == "+":
        return v1+v2
    elif operation == "-":
        return v1-v2
    elif operation == "*":
        return v1*v2
    elif operation == "/":
        return v1/v2
    elif operation == "**":
        return v1**v2
    elif operation == "%":
        return v1%v2
    else:
        return "Invalid operation"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Solve expressions                                                             
#-------------------------------------------------------------------------------

#Calulates operations that can have parenthesis
#Solves them in a sort of recursive way. When one or more arguments are lists
#calls solveExpressions until only two numbers are sent as parameters
def doComplexOperation(value1, value2, operation):
    v1 = 0
    v2 = 0
    if type(value1) == list:
        v1 = solveExpression(value1)
    else:
        v1 = float(value1)
    if type(value2) == list:
        v2 = solveExpression(value2)
    else:
        v2 = float(value2)
    
    return doOperation(v1, v2, operation)
    

    
#Solves a full equation having in mind the following precedence 
# Note: (Higher number represents a higher precedence):
# 3 -> **
# 2 -> * / %
# 1 -> - +
def solveExpression(expression):
    i = 0
    if len(expression) == 1:
        return solveExpression(expression[0])
    while i < len(expression):
        if expression[i] == "**":
            value = doComplexOperation(expression[i-1], expression[i+1], expression[i])
            expression[i] = value
            del expression[i+1]
            del expression[i-1]
            i = -1
        i += 1
    i = 0
    while i < len(expression):
        if expression[i] == "*" or expression[i] == "/" or expression[i] == "%":
            value = doComplexOperation(expression[i-1], expression[i+1], expression[i])
            expression[i] = value
            del expression[i+1]
            del expression[i-1]
            i = -1
        i += 1
    i = 0    
    while i < len(expression):
        if expression[i] == "+" or expression == "-":
            value = doComplexOperation(expression[i-1], expression[i+1], expression[i])
            expression[i] = value
            del expression[i+1]
            del expression[i-1]
            i = -1
        i += 1
    return expression[0]



#-------------------------------------------------------------------------------





#-------------------------------------------------------------------------------
# Function that calculates the value of an expressions with only 2 values
#-------------------------------------------------------------------------------
def twoValueExpression():
    v1_str = input("First variable: ")
    v2_str = input("Second variable: ")
    operation = input("Operation: ")

    try:
        v1 = float(v1_str)
        v2 = float(v2_str)

        result = doOperation(v1, v2, operation)
        print(result)
    except:
        print("Invalid values!")
#-------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#Parses expressions in order to facilitate solving them.
#Separates values and operatotion symbols into different elements of a list
#Values between parenthesis are put in lists of lists
def parseExpression(expression):
    result = []
    count = 0
    while count < len(expression):
        if expression[count] == "(":
            count += 1
            aux = 0
            sub_expression = ""
            while count < len(expression):
                if expression[count] == "(":
                    aux += 1
                if expression[count] == ")":
                    aux -= 1
                if aux == -1 and expression[count] == ")":
                    result.append(parseExpression(sub_expression))
                    count+=1
                    break
                
                sub_expression += expression[count]
                count += 1
            continue
        else:
            sub_string = expression[count]
            if expression[count].isnumeric():
                count += 1
                while count < len(expression):
                    if expression[count].isnumeric() or expression[count] == ".":
                        sub_string += expression[count]
                    else:
                        count -= 1
                        break
                    count += 1
            elif expression[count] == "*":
                if count + 1 < len(expression) and expression[count+1] == "*":
                    sub_string += "*"
                    count += 1
            result.append(sub_string)
        count+=1
    return result
#-------------------------------------------------------------------------------

#Solves a full expression and returns a value 
def fullExpression():
    expression_str = input("Introduce the expression: ")
    expression_str = expression_str.replace(" ", "")
    
    expression_list = parseExpression(expression_str)
    print(solveExpression(expression_list))

def start():

    option = "-1"
    while option != "3":
        option = input("1 - 2 Value expression\n" \
                       "2 - Full expression\n" \
                       "3 - Exit\n")
        if option == "1":
            twoValueExpression()
        elif option == "2":
            fullExpression()
        elif option == "3":
            return
        else:
            print("No valid option selected")
