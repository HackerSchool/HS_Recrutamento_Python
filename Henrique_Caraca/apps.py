# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:25:52 2021

@author: User
"""

from app_calculadora import main_cal
from app_chatbot import main_cb
from classe_tictactoe import main_ttt

def menu_apps():
    # menu onde o utilizador escolhe que app quer utilizar
    while True:
        print('--------------------------')
        print('''\nEscolha a aplicação:
              1 - Calculadora
              2 - Chat Bot
              3 - Tic-Tac-Toe
              4 - Voltar atrás
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            main_cal()
        elif opcao == '2':
            main_cb()
            pass
        elif opcao == '3':
            main_ttt()
        elif opcao == '4':
            return
        
        else:
            print('\nOpção não válida')
            

    