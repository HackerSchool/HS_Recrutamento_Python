# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:46:08 2021

@author: luis_
"""
import time
from calculadora import calculadora
from chat_bot import chat_bot
from tic_tac_toe import tic_tac_toe
from mudar_password import mudar_password


def menu_login(utilizador,utilizador_password):
    
    
    p = True
    
    while p == True:
        try:
            print(chr(27) + "[2J") # Limpa o terminal 
            
            print("\n| ------ Menu Login ------ |")
            print("| 1. Calculadora           |")
            print("| 2. Chat-Bot              |")
            print("| 3. Tic-Tac-Toe           |")
            print("| 4. Mudar password        |")
            print("| 5. Logout                |")
            print("|--------------------------|")
            
            opcao_login = int(input("Introduza a opção : "))        # Menu com várias funções associadas, uma função para cada opção
            if opcao_login == 1:
                print("OK")
                calculadora()
                print(chr(27) + "[2J")
                
            elif opcao_login == 2:
                print("OK")
                chat_bot(utilizador)
                print(chr(27) + "[2J")
                
            elif opcao_login == 3:
                print("OK")
                tic_tac_toe()
                print(chr(27) + "[2J")
                
            elif opcao_login == 4:
                print("OK")
                mudar_password(utilizador,utilizador_password)
                print(chr(27) + "[2J")
                
                
            elif opcao_login == 5:                                  # O logout é feito recorrendo ao break, deste modo o loop acaba e voltamos ao menu principal
                print("OK")
                print(chr(27) + "[2J") # Limpa o terminal 
                time.sleep(0.5)
                break
            else: 
                 print("Erro , introduza um número entre 1 e 5 ")
            
        except:
            print("Erro , introduza um número entre 1 e 5 ")