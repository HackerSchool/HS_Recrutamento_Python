# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:20:59 2021

@author: luis_
"""
import time

def Registar():
    
    print(chr(27) + "[2J")                                  # Limpa o terminal antes de perguntar as credenciais
    time.sleep(0.5)
    novo_utilizador = str(input("Novo utilizador: "))       # Introduzir um novo utilizador
    nova_password = str(input("Nova password: "))           # Introduzir uma nova password
    
    while novo_utilizador == "" or nova_password == "":     # Enquanto as variaveis estiverm vazias , volta a perguntar até que deixe de ser verdade
        print(chr(27) + "[2J")                              # Limpa o terminal antes de perguntar as credenciais
        time.sleep(0.5)
        novo_utilizador = str(input("Novo utilizador: "))
        nova_password = str(input("Nova password: "))
        
    novo_utilizador_password = str( novo_utilizador + ","+ nova_password)  # Junta as variaveis espaçadas por uma "," para poder adicionar no ficheiro "credenciais.txt" no mesmo formato dos dados existentes
    credenciais = open ("credenciais.txt","a")                              # Abre o ficheiro no modo append
    
    credenciais.write(novo_utilizador_password + '\n')                      # Escreve no ficheiro uma nova linha com os novos dados          
    print("Utilizador adicionado com sucesso!")                             # Utilizador adicionado com sucesso!
    return
