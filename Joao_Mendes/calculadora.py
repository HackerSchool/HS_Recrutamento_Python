'''Transformar string em lista'''

def tratamento_lista(string):
    aux1 = string.split()
    for i,c in enumerate(aux1):
        if c.startswith('('): #Separa parenteses de numero
            aux1[i:i] = c[0] #Cria novo elemento com parenteses
            aux1[i+1] = c[1:] #Muda elemento para numero
        elif c.endswith(')'):
            aux1[i:i] = c[-1:] #Cria novo elemento com parenteses na posicao dos numeros
            aux1[i+1] = c[:-1] #Muda elemento para numero na posicao dos parenteses
        else:
            continue
        
    reversed_aux = aux1[::-1]
    for j,c1 in enumerate(reversed_aux):
        if c1.find(')') != -1:
            reversed_aux[j-1],reversed_aux[j] = reversed_aux[j],reversed_aux[j-1] #troca numero com parenteses
        else:
            continue
    aux1 = reversed_aux[::-1]
    return aux1
    

'''Transformar string em lista'''

def parenteses(aux1):     
    while True:
        n_par = 0
        list_length = len(aux1)
        for position,c in enumerate(aux1):
            if c == '(':
                p = position
            elif c == ')':
                aux1[p:position+1] = calculo_regras(aux1[p+1:position]) #calculo da lista na lista dentro dos parenteses
                break
            else:
                n_par += 1
                continue
        if n_par == list_length:
            break
            
    return aux1
            
    
'''Ordenar as operacoes'''
    
def calculo_regras(aux):
    num = [float(aux[i]) for i in range(0,len(aux),2)] #Separa lista em numeros e operacoes
    op = [aux[i] for i in range(1,len(aux),2)]
    num,op = exponencial(num, op)
    num,op = mult(num, op)
    num,op = div(num, op)
    num,op = div_int(num, op)
    num,op = resto(num, op)
    num,op = soma(num, op)
    num,op = subtr(num, op)
    return num
    

'''Funcoes para fazer operacoes'''

#exponencial
def exponencial(num, op):
    for i in range(len(op)):
        while op[i]  == '**':
            num[i:i+2] = [num[i] ** num[i+1]] #transforma dois numeros num numero (resultado)
            op[i] = [] #transforma operador usado em lista vazia
            print (num,op)
            if len(num) == 1: #se resultado for obtido terminar loop
                break
        else:
            continue
        if len(num) == 1: #resultado obtido implica fim do loop
            break
    op = [i for i in op if i != []] #apaga listas vazias
    return num,op
      
#multiplicacao (funcionamento analogo ao exponencial)
def mult(num, op):
    for i in range(len(op)):
        while op[i]  == '*':
            num[i:i+2] = [num[i] * num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op    
    
#divisao (funcionamento analogo ao exponencial)
def div(num, op):
    for i in range(len(op)):
        while op[i]  == '/':
            num[i:i+2] = [num[i] / num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op

#divisao inteira (funcionamento analogo ao exponencial)
def div_int(num, op):
    for i in range(len(op)):
        while op[i]  == '//':
            num[i:i+2] = [num[i] // num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op
        
#resto (funcionamento analogo ao exponencial)
def resto(num, op):
    for i in range(len(op)):
        while op[i]  == '%':
            num[i:i+2] = [num[i] % num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op
        
#soma (funcionamento analogo ao exponencial)
def soma(num,op):
    for i in range(len(op)):
        while op[i]  == '+':
            num[i:i+2] = [num[i] + num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op
       
#subtracao (funcionamento analogo ao exponencial)
def subtr(num,op):
    for i in range(len(op)):
        while op[i]  == '-':
            num[i:i+2] = [num[i] - num[i+1]]
            op[i] = []
            if len(num) == 1:
                break
        else:
            continue
        if len(num) == 1:
            break
    op = [i for i in op if i != []]
    return num,op


'''Menu da Calculadora'''

def calculadora_1():
    while True:
        print('''\nCalculadora:\n
          Escolha as suas opções:
              1 - Cálculo de expressão com múltiplas operações
              2 - Ir para o menu de Login\n''')
        escolha = input("Opção: ")
        if escolha == '1':
            print ('''\nNOTA 1: Separar operadores e números com um "espaço" para calcular resultado
            NOTA 2: No entanto, os parenteses podem estar juntos aos números
            Exemplo: ((3 + 7) * 4 / (7 - 5))''')
            string = input("Expressão a calcular: ")
            aux = tratamento_lista(string)
            aux = parenteses(aux)
            resposta = calculo_regras(aux)
            print("\nResultado = ", resposta[0])
        elif escolha == '2':
            break
        else:
            print("\nOpção não existe\n")