import apps.Calculator.basic_operations as basic_operations
import apps.Calculator.equation_solver as equation_solver

def print_calculator_menu(selector):
    print("=====================================")
    print("1 - normal operations")
    print("2 - evaluate expression")
    print("3 - evaluate equation")
    print("4 - Go back")
    print("=====================================")

    a = input()

    if a == "1":
        num1 = eval(input("Num 1: "))
        num2 = eval(input("Num 2: "))
        op = input("Operator: ")
        try:
            print(basic_operations.basic_calculator(num1,num2,op))
        except Exception as ex:
            print(str(ex))
    elif a == "2":
        print("Please insert the expression")
        print("note: use parentheses to avoid ambiguities")
        expression = input("> ")
        try:
            print(basic_operations.evaluate_expression(expression))
        except Exception() as ex:
            print(str(ex))
    elif a == "3":
        print("Please insert the expression")
        print("IMPORTANT: if a value is negative please input the - sign right \
            before the number. Ex: 4x = -56x -10x + 2")
        expression = input("> ")
        print(equation_solver.evaluate_expression(expression))
    elif a == "4":
        selector.goBack()