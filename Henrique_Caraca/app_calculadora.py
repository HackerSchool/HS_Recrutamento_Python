# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:57:09 2021

@author: User
"""

def operacao1():
    # recebe dois numeros (n1 e n2) e uma operacao (op)
    # dá print do resultado de  n1 op n2
    n1 = float(input('Primeiro número: '))
    op = input('Escolha a operaçao (+, -, x, /, **, %): ')
    n2 = float(input('Segundo número: '))
    if op == '+': print('Resultado: {}'.format(n1+n2))
    elif op == '-': print('Resultado: {}'.format(n1-n2))
    elif op == 'x': print('Resultado: {}'.format(n1*n2))
    elif op == '/': print('Resultado: {}'.format(n1/n2))
    elif op == '**': print('Resultado: {}'.format(n1**n2))
    elif op == '%': print('Resultado: {}'.format(n1%n2))
    else:
        print('Operação não existe')
    a = input('(pressionar q  para sair)')
    if a!='q': operacao1()
    
######################################

def s_op(n2,op,n1):
    # input de dois numeros (n2 e n1) e uma operacao (op)
    # dá print do resultado de  n1 op n2
    n1,n2 = float(n1), float(n2)
    if op == '+': return n1+n2
    elif op == '-': return n1-n2
    elif op == 'x': return n1*n2
    elif op == '/': return n1/n2
    elif op == '*': return n1**n2
    elif op == '%': return n1%n2


def get_val_op(s):
    # da return da prioridade de uma certa operação
    if s in 'x/%': val=2
    elif s in '+-': val = 1
    elif s == '*': val = 3
    else: val = 0
    
    return val


def cal(exp):
    
    #tirar espaços
    exp = exp.split(' ')
    exp = ''.join(exp)
    #garantir que o termo '**' foi substituído por '*'
    exp = exp.replace('**','*')
    stack = [] # guardar todas as operações e números
    num = ''
    for a in exp:
        if a == '*' and num[0]=='-':
            # de forma geral a operação menos é tratado como a soma de um número negativo
            # é preciso alterar esse comportamento quando se tem uma potencia
            # pois 2-7**2 != 2+(-7)**2
            if stack:
                stack.pop() # retirar o +
            else:
                # se o 1o termo for um número negativo tem de se passar para 0-(o número negativo)
                stack.append('0')
                
            stack.append('-')
            num = num[1:]
            
        if a in ['+','x','/' ,'%', '*']:
            stack.append(num)  # fim de um número
            stack.append(a)  # acrescentar uma operação
            num = ''  # início de um novo número
        elif a == '-':
            if num == '-': # menos com menos dá mais
                num = ''
            elif num:  # passar o - num para + (-num)
                stack.append(num)
                stack.append('+')
                num = '-'
            else:
                num='-'

        else:
            num+=a # acrescentar o final ao num
    if num:
        stack.append(num)

    
    max_ = 0 # valor da operação com maior prioridade
    stack2 = []  # guardar operações que vai acumular operações e números até atingir um menor grau de prioridade
    for s in stack:

        val = get_val_op(s)
        
        if val > max_:
            max_=val
        elif val>0: #grarantr que é uma operação e não um número
            while len(stack2)>1 and get_val_op(stack2[-2]) >= val and val!=3: # se a prioridade descer deve-se realizar todas as operações com prioridade superior
                max_ = val
                stack2.append(s_op(stack2.pop(), stack2.pop(),stack2.pop()))

        stack2.append(s)

   
        
    while len(stack2)>1: #fazer operações até o stack ter um valor (o resultado)
        stack2.append(s_op(stack2.pop(), stack2.pop(),stack2.pop()))
    return stack2[0]
   

        
    

def cal2(exp):
    exp = exp.replace('**','*')  # tornar o símbolo '**' num só carater '*'
    i = 0
    stack = [] # guarda as posições dos '('
    while i<len(exp):
        # detetar os parenteses e resolver isso primeiro
        if exp[i] == '(':
            stack.append(i)
        if exp[i] == ')':
            inicio = stack.pop()
            parenteses = cal(exp[inicio+1: i])  # resolve os parenteses
            exp = exp[:inicio] + str(parenteses) + exp[i+1:] #acrescenta o resultado à expressão
            i=inicio-1 + len(str(parenteses)) # coloca o i no sítio certo 
        i+=1

    return cal(exp)


def operacao2():
    # cal2 mas só com uma operação
    exp = input('Escreva a expressão a calcular:  (+, -, x, /, **, %)\n')
    res = cal2(exp)
    print("O resultado é: ", res)
    a = input('(pressionar q  para sair)')
    if a!='q': operacao2()

##################################

def main_cal():
    print("Bem-vindo à calculadora\n")
    while True:
        print('''\nEscolhe a tua opção:
              1 - Simples Operação
              2 - Expressão
              q - Sair
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            operacao1()
        elif opcao == '2':
            operacao2()
        elif opcao == 'q':
            print("A sair")
            break
        else:
            print("Opcao não válida")
            
#main_cal()