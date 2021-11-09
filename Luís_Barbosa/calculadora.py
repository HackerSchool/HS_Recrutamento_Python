# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:13:34 2021

@author: luis_
"""

import time
#import matplotlib.pyplot as plt
#import numpy as np


def calcular():                                                     # Calcula expressões com dois números
    
    expressao = str(input("Introduza a expressão ( 1 + 1 ) : "))   # Pede para ser introduzida uma expressão na forma 1 espaço + espaço 1, variavel é guardada com uma string
    
    lista = expressao.split()                                       # Separar a string anterior numa lista
    
    print(lista)
    
    
    numero_1, operador, numero_2 = lista                            # atribuir as variaveis numero_1 , numero_2 e operador aos elementos da lista
    
    numero_1_convertido = float(numero_1)                           # converter os números de string para float(inteiros e decimais)  
    numero_2_convertido = float(numero_2)
    
    
    if operador == "+":                                             # Se for detetado um + na expressão então soma o numero 1 com o numero 2  (igual para as outras opções)
        resultado = numero_1_convertido + numero_2_convertido
    elif operador == "-":
        resultado = numero_1_convertido - numero_2_convertido
    elif operador == "/":
        resultado = numero_1_convertido / numero_2_convertido
    elif operador == "*":
        resultado = numero_1_convertido * numero_2_convertido
    else:
        print("Erro !!! Introduza um operador válido (+ - / *)  ")         # Se não for detetado nenhum dos operadores anteriores
        
        time.sleep(2)
        
        return calcular()
            
        

    print(resultado)
    
    time.sleep(5)

def resolver_equação_2_grau():                                      # Resolve equações de 2º grau com a fórmula resolvente
    
    print(" ---- Resolução equações 2º grau ---- ")
    
    print("Equação na forma : ax^2 + bx + c = 0 ")
    
    a = float(input("Introduza o valor de a :"))                    # Pede valores em float (inteiros e decimais)
    b = float(input("Introduza o valor de b :"))
    c = float(input("Introduza o valor de c :"))
    
        
    while a == "" or b == "" or c == "":                            # Se as variaveis a,b,c estiverem em "branco", volta a pedir
    
            a = float(input("Introduza o valor de a :"))
            b = float(input("Introduza o valor de b :"))
            c = float(input("Introduza o valor de c :"))
    
    x1 = ((-b+((b**2)-4*a*c)**0.5)/(2*a))                           # Fórmula resolvente para equações de 2º grau
    
    x2 = ((-b-((b**2)-4*a*c)**0.5)/(2*a))                           # Fórmula resolvente para equações de 2º grau

    print(x1)
    print(x2)
    
    time.sleep(5)                                                   # Espera 5 s , para o utilizador poder ver o resultado , caso contrário é processado tão rápido que nem se vê
    
#def gráfico_funções():                                             # Fazer gráficos de funções
    
#def calculo_matrizes():                                            # Fazer cálculo de matrizes
    
    
    
    





def calculadora():
    
    c = True
    
    while c == True:
        try:
            print(chr(27) + "[2J") # Limpa o terminal 
            
            print("\n| --------- Calculadora ---------- |")
            print("| 1. Calcular                      |")
            print("| 2. Resolução equações 2º grau    |")
            print("| 3. Gráfico funções               |")
            print("| 4. Cálculo de matrizes           |")
            print("| 5. Sair                          |")
            print("|----------------------------------|")
            
            opcao_login = int(input("Introduza a opção : "))        # Menu igual aos outros
            
            if opcao_login == 1:
                print("OK")
                calcular()
                print(chr(27) + "[2J")
                
            elif opcao_login == 2:
                print("OK")
                resolver_equação_2_grau()
                print(chr(27) + "[2J")
                
            elif opcao_login == 3:
                print("OK")
                #gráfico_funções()
                print(chr(27) + "[2J")
                
            elif opcao_login == 4:
                #calculo_matrizes()
                print("OK")
               
                print(chr(27) + "[2J")
                
                
            elif opcao_login == 5:
                print("OK")
                print(chr(27) + "[2J") # Limpa o terminal 
                time.sleep(0.5)
                break
            else: 
                 print("Erro , introduza um número entre 1 e 5 ")
            
        except:
            print("Erro , introduza um número entre 1 e 5 ")
    
            