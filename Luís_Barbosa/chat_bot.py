# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:13:50 2021

@author: luis_
"""
import time
from chat import chat


def chat_bot(utilizador):
    
    b = True
    
    while b == True:
        try:
            print(chr(27) + "[2J") # Limpa o terminal
            
            print("\n| ------ Chat-Bot -------  |")
            print("| 1. Chat                  |")
            print("| 2. Sair                  |")
            print("|--------------------------|")
            
            opcao_login = int(input("Introduza a opção : "))            # Menu igual aos outros
            if opcao_login == 1:
                print("OK")
                chat(utilizador)                                        # chat precisa da variável "utilizador" que vem do login no programa
                print(chr(27) + "[2J")
                
            elif opcao_login == 2:
                print("OK")
                print(chr(27) + "[2J") # Limpa o terminal 
                time.sleep(0.5)
                break
                
            else: 
                 print("Erro , introduza um número entre 1 e 5 ")
            
        except:
            print("Erro , introduza um número entre 1 e 5 ")