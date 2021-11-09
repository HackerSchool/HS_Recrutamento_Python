def basic_calculator(num1,num2,op):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        if (num2 == 0):
            raise Exception("Cannot devide by 0")
        else:
            return num1/num2
    elif op == "%":
        return num1%num2
    elif op == "^":
        return num1**num2
    else:
        raise Exception("Unknown operator")

def evaluate_expression(expression):
    operands_and_operations = expression.split(" ")
    
    # A operação que vamos fazer nunca pode estar dentro de paranteses
    # dessa forma sabemos que estamos a calcular o operador cert
    # (1+2)*(3)

    parenteses = False
    for i in range(len(expression)):
        if expression[i] == "(":
            parenteses = True
        elif expression[i] == ")":
            parenteses = False
        if ((expression[i] in ("+","-","*","/","^")) and not parenteses):
            # [(1+2),3]

            # [(1+2)]
            operand1 = expression[:i]
            # [3]
            operand2 = expression[i+1:]

            try:
                operand1 = eval(operand1)
            except NameError():
                operand1 = evaluate_expression(operand1)
            
            try:
                operand2 = eval(operand2)
            except NameError():
                operand2 = evaluate_expression(operand2)

            return basic_calculator(operand1, operand2, expression[i])

# print(evaluate_expression("(1+2)*3"))
# print(evaluate_expression("(2+2)+(2+2)*2"))
# print(evaluate_expression("(2*(3+3))/(5-2+1)"))
