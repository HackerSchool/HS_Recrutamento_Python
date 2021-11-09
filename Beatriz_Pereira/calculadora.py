

def calcmain(nomedeutilizador,palavrapasse):
    print("Escolhe uma ação:\n 1-Inserir dois números e um operador\n 2-Inserir uma expressão matemática (máximo de um operador)\n")
    opcao=input("Ação:\n")
    if opcao=='1':
        calc1()
    if opcao=='2':
        calc2()   
    return 0

def calc1():
    res=0
    a=input("Insere o primeiro número:\n")
    b=input("Insere o segundo número:\n")
    op=input("Escolhe uma das seguintes operações: +,-,x,/,**,%\n")
    if op == '+': #este conjunto de ifs verifica o tipo de operador e faz a conta
        res=float(a)+float(b)
        print(res)
        return res
    if op == '-':
        res=float(a)-float(b)
        print(res)
        return res
    if op == 'x':
        res=float(a)*float(b)
        print(res)
        return res
    if op == '/':
        res=float(a)/float(b)
        print(res)
        return res
    if op == '**':
        res=float(a)**float(b)
        print(res)
        return res
    if op == '%':
        res=float(a)%float(b)
        print(res)
        return res
    else:
        print("Operador inválido")

def calc2():
    strinput=input("Insere uma expresão matemática espaçada entre número e operador (máximo de um operador):\n")
    lista=strinput.split(' ') #mete a expressao numa lista, dividindo nos espaços i.e 3 + 4 [3,+,4]
    if len(lista) != 3: #como se trata so de uma expressao com um operador o tamanho da lista é sempre 3
        print("Entrada inválida")
        return 0
    if lista[1] == '+': #este conjunto de ifs verifica o tipo de operador e depois transforma as posições com numeros em floats e faz a operação
        res=float(lista[0])+float(lista[2])
        print(res)
        return res
    if lista[1] == '-':
        res=float(lista[0])-float(lista[2])
        print(res)
        return 
    if lista[1] == 'x':
        res=float(lista[0])*float(lista[2])
        print(res)
        return res
    if lista[1] == '/':
        res=float(lista[0])/float(lista[2])
        print(res)
        return res
    if lista[1] == '**':
        res=float(lista[0])**float(lista[2])
        print(res)
        return res
    if lista[1] == '%':
        res=float(lista[0])%float(lista[2])
        print(res)
        return res
    else:
        print("Entrada inválida")


