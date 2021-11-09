# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:16:37 2021

@author: luis_
"""
import time

def mudar_password(utilizador,utilizador_password):                             # Função dependente de dados do login
    
    
    utilizador_nova__password = str(utilizador + "," + input("Introduza a nova password: "))  # perguntar nova password e introduzir numa variavel com o mesmo formato dos dados no ficheiro "credenciais.txt"
    
    
    with open("credenciais.txt","r") as f:                                      # Abrir ficheiro no modo de leitura
        newline=[]                                                              # Criar uma lista em branco
        for word in f.readlines():                                              # Ler a linhas no ficheiro e verificar que o utlizador está no ficheiro
            newline.append(word.replace(utilizador_password,utilizador_nova__password))  ## Procura a linha correta e escreve a password
        
    #print("A")
        
    with open("credenciais.txt","w") as f:
            for line in newline:
                f.writelines(line)                                              # Escreve e guardo o ficheiro como a nova password
                
    print("Password alterada com sucesso!")
    time.sleep(0.5)
    
    
    
     
    
       
