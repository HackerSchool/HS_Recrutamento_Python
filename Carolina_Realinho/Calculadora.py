# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:20:00 2021

@author: Carolina
"""
def calculadora():
    print("Bem vindo à Calculadora!")
    
    '''
    Esta é uma calculadora simples e com ela podemos fazer a: adição(+),
    subtração(-), multiplicação(*), divisão(/), potenciação(**), divisão inteira(//)
    e resto da divisão(%) de dois números.
    Para tal, os dados devem ser introduzidos do seguinte modo:
        n1(espaço)(operação)(espaço)(n2)
        Por exemplo: 2 + 5
                     3 ** 2   
    Após o retorno do resultado, é possível escolher se se pretende continuar a 
    calcular ou se se pretende voltar ao menu de login.
    '''
    
    continuar = True
    
    while continuar==True:
        conta = input("\nIntroduza a expressão com uma operação a calcular: ")
        
        conta_separada = conta.split()
        
        if conta_separada[1]=="+":
            resultado = float(conta_separada[0]) + float(conta_separada[2])
            print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="-":
            resultado = float(conta_separada[0]) - float(conta_separada[2])
            print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="*":
            resultado = float(conta_separada[0]) * float(conta_separada[2])
            print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="/":
            if float(conta_separada[2]) == 0:
                print("Erro matemático.")
            else:
                resultado = float(conta_separada[0]) / float(conta_separada[2])
                print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="**":
            resultado = float(conta_separada[0]) ** float(conta_separada[2])
            print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="//":
            if float(conta_separada[2]) == 0:
                print("Erro matemático.")
            else:
                resultado = float(conta_separada[0]) // float(conta_separada[2])
                print(f"{conta} = {round(resultado,4)}")
        elif conta_separada[1]=="%":
            if float(conta_separada[2]) == 0:
                print("Erro matemático.")
            else: 
                resultado = float(conta_separada[0]) % float(conta_separada[2])
                print(f"{conta} = {round(resultado,4)}")
       
        escolha = input("\nPressione '0' para continuar. Qualquer outro para sair. ")
        if escolha != '0':
            continuar == False
            break