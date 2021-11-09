# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:22:12 2021

@author: User
"""

from apps import menu_apps


def read(identificador):
    # dá return da palavra passe de utilizador se existir
    # caso o utilizador não exista dá return de False
    ficheiro = open('registos.txt', 'r')

    for linha in ficheiro:
        identificador2 = linha.split(';')
        if identificador == identificador2[0]:
            conteudo = identificador2[1]
            ficheiro.close()
            return conteudo

    ficheiro.close()
    return False


def write(identificador, conteudo):
    # acrescenta "identificador;conteudo;"" no fichero registos.txt
    ficheiro = open('registos.txt', 'a')
    ficheiro.write(identificador+ ';' + conteudo + ';\n')
    ficheiro.close()

def login():
    # faz o login do utilizador
    print('--------------------------')
    success = False  # flag ou password
    while not success:
        # recebe o username
        username = input("Username:  (q to quit)\n")
        if username == 'q': return
        success = read(username)
        if not success:
            print("Esse user name não existe, vamos tentar outra vez")
    for i in range(3):
        # 3 tentativas para acertar a palavra passe
        password = input("Password:   (q to quit)\n")
        if password == 'q': return
        if password==success:
            menu(username)
            return 
        
        else:
            print('Password errada')
            print(f'Tem mais {2-i} tentativas')
            
    if password != success:
        #expiraram o número de tentativas
        print('Expirou o número de tentativas')
    
    
def mudar_pass(identificador):
    # função para mudar a palavra passe
    print('--------------------------')
    while True:
        # recebe a palavra passe e verifica se é válida
        nova_pass = input("Insira a nova palavra-passe:\n")
        if nova_pass != 'q' and nova_pass != '':
            break
        print('Palavra-passe não válida')
    ficheiro = open("registos.txt", "r")  
    replacement = ""
    for linha in ficheiro:
        # loop pelo ficheiro para reescrevê-lo com a mudança na palavra passe
        identificador2 = linha.split(';')
        linha = linha.strip()
        if identificador == identificador2[0]:
            linha = identificador2[0] + ';' + nova_pass + ';' 
        replacement += linha + "\n"
    ficheiro.close()
    fout = open("registos.txt", "w")
    fout.write(replacement)
    fout.close()
    
    
def menu(user):
    # menu depois do login
    while True:
        print('--------------------------')
        print('''\nEscolha o que quer fazer:
              1 - Aplicação
              2 - Mudar a palavra-passe
              3 - Fazer logout
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            menu_apps()
        elif opcao == '2':
            mudar_pass(user)
        elif opcao == '3':
            print('Logging out')
            return
        else:
            print('\nNão percebi, pode repetir?')
    
    

       
def registar():
    # acrescentar um novo utilizador
    print('--------------------------')
    while True:
        # receber um nome de utilizador válido
        novo_user = input("Insira um username:\n")
        if not read(novo_user) and novo_user != 'q' and novo_user != '':
            break
        print('Username já existente')
    while True:
        # receber uma palavra passe válida
        nova_pass = input("Insira uma palavra-passe:\n")
        if nova_pass != 'q' and nova_pass != '':
            break
        print('Palavra-passe não válida')
        
    write(novo_user,nova_pass)

    

    
def main():
    # primeiro menu que aparece
    print('Bem vindo')
    while True:
        print('--------------------------')
        print('''\nEscolha o que quer fazer:
              1 - Login
              2 - Registar
              3 - Sair
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            login()
        elif opcao == '2':
            registar()
        elif opcao == '3':
            print('Até à próxima!')
            break
        else:
            print('Não percebi, pode repetir?')
            
            
main()