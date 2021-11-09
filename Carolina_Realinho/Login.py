# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:26:44 2021

@author: Carolina
"""

def validar_opcao():
    opcao = int(input("Menu:\n1 - Login\n2 - Registar\n3 - Sair do programa\n\nSelecione a opção desejada: ")) 
    while (opcao!=1 and opcao!=2 and opcao!=3):
        print("\nErro. Opção inválida.")
        opcao = int(input("Selecione novamente: "))
        if (opcao==1 or opcao==2 or opcao==3):
            break
    return opcao

def registar_nome_de_utilizador(lista1):    
    username = input("\nNome de utilizador: ")    
    username_valido = True
      
    for nome in lista1:
        if nome == username:
            username_valido = False
            print("Nome de utilizador indisponível.")
            break
   
    while username_valido == False:
        username = input("\nNome de utilizador: ")
        for nome in lista1:
            if nome == username:
                username_valido = False
                print("Nome de utilizador indisponível.")
                break
            else:
                return username
    if username_valido == True:
        return username

def registar_palavra_passe():
    password = input("\nPalavra passe: ")
    password_valida = True
    
    if len(password)<8 or len(password)>20:
        password_valida = False
        print("A palavra passe deve ter entre 8 e 20 caracteres.")
            
    while password_valida == False:
        password = input("\nPalavra passe: ")
        if len(password)<8 or len(password)>20:
            password_valida = False
            print("A palavra passe deve ter entre 8 e 20 caracteres.")
        else:
            return password
    if password_valida == True:
        return password

def validar_credenciais(username, lista1, lista2):
    password = input("\nPalavra passe: ")
    
    if username in lista1:
        if password in lista2:
            if password == lista2[lista1.index(username)]:
                return True
            else:
                print("Password incorreta")
                return False
        else:
            print("Password incorreta")
            return False
    else:
        print("Utilizador não encontrado.")
        return False

def menu_login():
    opcao = int(input("Menu:\n1 - Calculadora\n2 - Chat Bot\n3 - Mudar palavra passe\n4 - Logout\n\nSelecione a opção desejada: ")) 
    while (opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4):
        print("\nErro. Opção inválida.")
        opcao = int(input("Selecione novamente: "))
        if (opcao==1 or opcao==2 or opcao==3 or opcao==4):
            break
    return opcao
               
opcao_valida = validar_opcao()
utilizadores = []
passes = []
import sys

while opcao_valida == 1 or opcao_valida == 2 or opcao_valida == 3:
    if opcao_valida == 1:
        username = input("\nNome de utilizador: ")
        entrar = validar_credenciais(username, utilizadores, passes)
        if entrar == True: #isto fará com que a "sessão expire", isto é, o utilizador terá que introduzir as suas credenciais novamente após sair das apps (penso que seja a coisa menos intuitiva na execução do programa)
            opcao = menu_login()
            
            if opcao == 1:
                sys.path.append('./Calculadora')
                import Calculadora  
                Calculadora.calculadora()
                opcao = menu_login()
            elif opcao ==2:
                sys.path.append('./Chatbot')
                import Chatbot  
                Chatbot.chat_bot()
                opcao = menu_login()
            elif opcao ==3:
                print("Introduza uma nova palavra passe.")       
                passes[utilizadores.index(username)] = registar_palavra_passe()
                print("\nPalavra passe alterada com sucesso.\nIntroduza as suas credenciais novamente.")           
            else:
                opcao_valida = validar_opcao()  
        else:
            opcao_valida = validar_opcao()  
        
    elif opcao_valida == 2:       
        utilizadores.append(registar_nome_de_utilizador(utilizadores))
        passes.append(registar_palavra_passe())
        print("\nUtilizador registado com sucesso.")
        opcao_valida = validar_opcao() 
        
    elif opcao_valida==3:
        sys.exit("A encerrar")