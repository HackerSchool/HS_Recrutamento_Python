# Cálculo com uma string e uma operação nela lida
def calculator_level_5():
    print("\n[RULE] Numbers and operations must be separated by a white space\n")
    exp = input("Expression: ")

    # Se a string não estiver vazia, é realizada a separação e a operação identificada, ficando a variável 'res' com o resultado
    if exp != '':
        num1 = exp.split(' ')[0]
        op = exp.split(' ')[1]
        num2 = exp.split(' ')[2]
        if op == '+':
            res = float(num1) + float(num2)
        elif op == '-':
            res = float(num1) - float(num2)
        elif op == 'x':
            res = float(num1) * float(num2)
        elif op == '/':
            res = float(num1) / float(num2)
        elif op == '**':
            res = float(num1) ** float(num2)
        elif op == '%':
            res = float(num1) % float(num2)
        print("\nResult: " + format(res))


# Cálculo com 2 números e 1 operação
def calculator_level_3():
    num1 = input("\nFirst number: ")
    num2 = input("Second number: ")

    print("\nAllowed opperations -> +, -, x, /, **, %")
    op = input("Operation: ")

    # A variável 'res' fica com o resultado da operação pedida
    if op == '+':
        res = float(num1) + float(num2)
    elif op == '-':
        res = float(num1) - float(num2)
    elif op == 'x':
        res = float(num1) * float(num2)
    elif op == '/':
        res = float(num1) / float(num2)
    elif op == '**':
        res = float(num1) ** float(num2)
    elif op == '%':
        res = float(num1) % float(num2)
    print("\nResult: " + format(res))



def calculator():
    print("\n-------------------------\n|                       |\n|    · Calculator ·     |\n|                       |\n|  1 - 2 Nums 1 Op (3)  |\n|                       |\n|  2 - 1 Str 1 Op (5)   |\n|                       |\n|  3 - Login Menu       |\n|                       |\n-------------------------\n")
    option = input("Type the option's number: ")

    if option == '1':
        calculator_level_3()
        calculator()
        return
    elif option == '2':
        calculator_level_5()
        calculator()
        return
    elif option == '3':
        return
    else:
        print("\n<ERROR> Unknown Option\n")
        calculator()    
    return