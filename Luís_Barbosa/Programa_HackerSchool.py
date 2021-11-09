# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:06:01 2021

@author: luis_
"""

## Login com apps

## Importar módulos

import time

from Login import Login
from Registar import Registar



t = True
while t == True:
    try:
        
                
        #print(chr(27) + "[2J") # Limpa o terminal 
        
        print("\n| --------- Menu --------- |")
        print("| 1. Login                 |")
        print("| 2. Registar              |")
        print("| 3. Sair do programa      |")
        print("|--------------------------|")
        
        opcao = int(input("Introduza a opção : "))          # Pretende-se que o utilizador só introduza números inteiros daí o uso do int()
        
        if opcao == 1:                                       # Se opção for 1, então aparece "ok" escrito no terminal e avança para a função Login()
            
            print("ok")
            
            Login()
            
           
        
        elif opcao == 2:                                    # Se opção for 2, então aparece "ok" escrito no terminal e avança para a função Registar()
            
            print("ok")
            
            Registar()
            
            
        
        elif opcao == 3:                                    # Se opção for 3, então aparece "A sair!" escrito no terminal e o loop termina fazendo com que o programa pare
            
            print("A sair!")
            
            break
        
        else: 
             print("Erro , introduza um número entre 1 e 3 ")      # Caso o número introduzido não esteja entre 1 e 3 , imprime o erro e o programa recomeça, dado que t é sempre verdade.
             time.sleep(1)
             

    except:
        print("Erro , introduza um número entre 1 e 3 ")           # Caso seja introduzida uma string,  imprime o erro e o programa recomeça, dado que t é sempre verdade.
                                                                    # O programa nunca bloqueia, mesmo que o utilizador não introduza um número entre 1 e 3 
        time.sleep(1)                                               # Importando o módulo time, usa-se para dar um delay depois de impressa a linha anterior, caso contrário o processo é tão rápido que o utilizador não conseguiria ver a mensagem de erro.
        
        
