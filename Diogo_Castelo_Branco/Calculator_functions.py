import time

def calculadora_nvl3(num1,num2,op):   # a calc nivel 3 foi utilizada como auxiliar para a calc nvl5

    if(op == '+'):
        return(num1 + num2)
    elif(op == '-'):
        return(num1 - num2)
    elif(op == 'x'):
        return(num1 * num2)
    elif(op == '/'):
        return(num1 / num2)
    elif(op == '*'):
        return(num1 ** num2)
    elif(op == '%'):
        return(num1 % num2)
    else:
        print("Não sei fazer isso")
        return -78965412365.31524

def calculadora_nvl5():

    continuar = '1'
    while(continuar == '1'):

        arg = input("\nInsere a operação na forma (num1 op num2)(atenção aos espaços!) com op=(+,-,x,/,**,%):\t")
        arg = arg.split()  #arg = 2 + 3   =>   arg = [2;+;3]
        
        sol = calculadora_nvl3(float(arg[0]),float(arg[2]),arg[1])

        if(sol != -78965412365.31524 ):     #se a calculadora tiver conseguido resolver a operação, manda o resultado
            print("Solução: ",sol)
        
        continuar = input("\nSe quiseres fazer outra operação prime 1. Caso contrário podes carregar em qualquer tecla para retornar ao menu login. ")
    else:
        print("A voltar ao menu login...")
        time.sleep(2)