# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:39:09 2021

@author: luis_
"""
## Definir a função Login()

import time

from menu_login import menu_login

def Login():
            print(chr(27) + "[2J")                                  # Limpa o terminal antes de perguntar as credenciais
            time.sleep(0.5)
            utilizador = str(input("Utilizador: "))                 # Pede o utilizador no formato string
            password = str(input("Password: "))                     # Pede a password no formato string
            
            while utilizador == "" or password == "":               #Enquanto as variaveis utilizador e password estiverem vazias, volta a pedir as variaveis
                print(chr(27) + "[2J")                              # Limpa o terminal antes de perguntar as credenciais
                time.sleep(0.5)
                utilizador = str(input("Utilizador: "))
                password = str(input("Password: "))
                
            
            credenciais = open ("credenciais.txt","r")              # Abre o ficheiro de dados "credenciais.txt" no modo de leitura
            read_credenciais = credenciais.read()                   # Lê o ficheiro e guarda numa variavel                     
            utilizador_password = str( utilizador + ","+ password)  # Converte os dados introduzidos para uma string na forma : "utilizador,password"
            
            ##print(utilizador_password)
            
            while True:
                                          
                if utilizador_password in read_credenciais:         # Se o utilizador e password forem encontrados no ficheiro, avança para a função menu_login
                    print("Bem-vindo!")
                    
                    menu_login(utilizador,utilizador_password)
                    
                    break                                           # Uma vez executada a função menu_login sai do while loop e volta ao menu inicial
                    
                else:
                    print("Login incorrecto")                       # Se o utilizador e password não forem encontrados no ficheiro, informa que o login está incorreto e tenta de novo
                    time.sleep(1)
                    
                    print(chr(27) + "[2J")
                    
                    utilizador = str(input("Utilizador: "))
                    password = str(input("Password: "))
                    
                    while utilizador == "" or password == "":
                        print(chr(27) + "[2J")                      # Limpa o terminal antes de perguntar as credenciais
                        time.sleep(0.5)
                        utilizador = str(input("Utilizador: "))
                        password = str(input("Password: "))
                        
                    credenciais = open ("credenciais.txt","r")
                    read_credenciais = credenciais.read()                       
                    utilizador_password = str( utilizador + ","+ password)
                    
                
                    
                    
                        
    
        