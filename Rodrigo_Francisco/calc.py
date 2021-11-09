import os



def isfloat(string):
    try:
        float(string)
    except ValueError:
        return 0
    return 1

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def parsing(todo, ans):
    parsed = []
    if(todo == "sair"):
        return(-1)
    if(todo == ""):
        return(1)

    if isfloat(todo.split()[0]):
        a = float(todo.split()[0])
        parsed.append(a)
    elif(todo.split()[0] == "ans"):
        parsed.append(ans)
    else:
        print("Número inválido! use um número ou ans")
        return(1)

    if (todo.split()[1] in "+-x/%" and len(todo.split()[1]) == 1) or (todo.split()[1] == "**"):
        parsed.append(todo.split()[1])
    else:
        print("\nOperação inválida! Use +,-,x,/,%,** para as operações")
        return(1)
    
    if isfloat(todo.split()[2]):
        b = float(todo.split()[2])
        parsed.append(b)
    elif(todo.split()[2] == "ans"):
        parsed.append(ans)
    else:
        print("Número inválido! use um número ou ans")
        return(1)
    
    return(parsed)

def meth(a, b, op):
    if(op == "+"):
        ans = a + b
    elif(op == "-"):
        ans = a - b
    elif(op == "x"):
        ans = a * b
    elif(op == "/"):
        if(b == 0):
            return "Erro matemático: divisão por zero."
        else:
            ans = a / b
    elif(op == "%"):
        if(b == 0):
            return "Erro matemático: divisão por zero."
        else:
            ans = a % b
    else:
        ans = a ** b
    return ans

def main(log, user):
    print("\nCalculadora")
    ans = 0
    print("\n- Introduza uma operação entre dois números separados por espaços\n- ans é o resultado da operação anterior\n- Escreva sair para sair da aplicação")
    while(True):
        todo = input(">  ").strip()

        parsed = parsing(todo, ans)

        if(parsed == 1):
            continue
        if(parsed == -1):
            break
        
        a = meth(parsed[0], parsed[2], parsed[1])
        if(a == "Erro matemático: divisão por zero."):
            print(a)
            continue
        ans = a
        if(ans - int(ans) == 0):
            print(int(ans))
        else:
            print(ans)

    clear()

