class Calculator:

    def run(self):
        while True:
            expression = input("Input Math expression or q to Quit\n")
            if expression == "q":
                return
            l = self.expression_to_list(expression)
            print(l)
            p = self.list_to_postscript(l)
            print(p)
            self.print_result(self.postscript_calculator(p))

    @staticmethod
    def expression_to_list(expression: str):
        l = expression.split()
        return l

    @staticmethod
    def postscript_calculator(postscript_list: list):
        stack = []
        try:
            for symbol in postscript_list:
                if symbol.isnumeric():
                    stack.append(float(symbol))
                else:
                    match symbol:
                        case "+":
                            stack[-2] = stack[-2] + stack[-1]
                        case "-":
                            stack[-2] = stack[-2] - stack[-1]
                        case "*":
                            stack[-2] = stack[-2] * stack[-1]
                        case "/":
                            stack[-2] = stack[-2] / stack[-1]
                        case "**":
                            stack[-2] = stack[-2] ** stack[-1]
                        case "%":
                            stack[-2] = stack[-2] % stack[-1]
                    stack.pop(-1)

            return stack
        except:
            return None

    @staticmethod
    def list_to_postscript(expression_list: list):
        postscript = []
        operators = []
        priority = []
        for symbol in expression_list:
            if symbol.isnumeric():
                postscript.append(symbol)
            else:
                match symbol:
                    case "+":
                        if len(operators) == 0:
                            operators.append("+")
                            priority.append(0)
                        else:
                            while priority[-1] > 0:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("+")
                            priority.append(0)
                    case "-":
                        if len(operators) == 0:
                            operators.append("-")
                            priority.append(0)
                        else:
                            while priority[-1] > 0:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("-")
                            priority.append(0)
                    case "*":
                        if len(operators) == 0:
                            operators.append("*")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("*")
                            priority.append(1)
                    case "/":
                        if len(operators) == 0:
                            operators.append("/")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("/")
                            priority.append(1)
                    case "%":
                        if len(operators) == 0:
                            operators.append("%")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("%")
                            priority.append(1)
                    case "**":
                        if len(operators) == 0:
                            operators.append("**")
                            priority.append(2)
                        else:
                            while priority[-1] > 2:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("**")
                            priority.append(2)
                    case "(":
                        operators.append("(")
                        priority.append(-1)
                    case ")":
                        while priority[-1] != -1:
                            postscript.append(operators.pop())
                            priority.pop()
                            if len(priority) == 0:
                                return None
                        priority.pop()
                        operators.pop()
                    case _:
                        return None

        while len(operators) > 0:
            operator = operators.pop()
            postscript.append(operator)
        print(postscript)
        return postscript

    @staticmethod
    def print_result(stack):
        if stack is None:
            print("Invalid Input")
        else:
            print(stack[0])
