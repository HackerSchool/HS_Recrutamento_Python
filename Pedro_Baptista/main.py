#Função que verifica se o username escolhido já existe, ou se a password inserida coincide com a do nome de utilizador inserido
#Tem como argumentos o nome e a password inseridos, e um inteiro que indica se se está a verificar apenas se o nome de utilizador 
#já existe ou se é para verificar se a password é a correta

from calculadora import calculadora as calculadora
from chatbot import chatbot as chatbot
from tictactoe import tictactoe as tictactoe

def verificadora(nick, passw, bit):

    fbase = open('base.txt','r')

    eol = "\n"
    passw = passw+eol

    for linha in fbase:

        nickV = linha.split(' ')[0]
        passwV = linha.split(' ')[1]

        if nickV == nick:
            if (bit == 0):
                fbase.close()
                return 0
            if (bit == 1):
                if passwV == passw:
                    fbase.close()
                    return 1
                else:
                    return 0

    fbase.close()

    if bit == 0:
        return 1

    if bit == 1:
        return 2



#função que apaga a linha que contém a password antiga, e insere uma linha nova com a password atualizada

def borracha(nick, passw):

    fbase = open('base.txt','r')
    linhas = fbase.readlines()

    fbase = open('base.txt','w')

    for linha in linhas:
        if linha != nick + ' ' + passw + '\n':
            fbase.write(linha)
    

    print('\nInsira a sua nova password\n')
    print('Inseriu:')
    passN = input()

    fbase = open('base.txt','a')
    fbase.write(nick + ' ' + passN + '\n')

    fbase.close()

    return passN

    

#Função que regista um novo utilizador

def registar():


    print('Insira o nome de utilizador que deseja\n')
    print('Inseriu:')
    nick = input()

    passw = '0'

    x = verificadora(nick, passw, 0)

    while x == 0:
        print('Esse username já existe! Deseja escolher outro ou voltar ao menu de login? Escreva "Sim" para esccolher outro nome ou "Sair" para voltar ao menu inicial\n')
        print('Inseriu:')
        answer = input()
        if answer == 'Sair':
            return()
        if answer == 'Sim':
            print('Insira o seu username\n')
            print('Inseriu:')
            nick = input()

        x = verificadora(nick, passw, 0)
        

    if x == 1:
        print('\nInsira a password que deseja\n')
        print('Inseriu:')
        passw = input()

    fbase = open('base.txt','a')
    fbase.write(nick + ' ' + passw + '\n')
    fbase.close() 


#Função que envia o utilizador para cada aplicação

def menuapps():
    	
    while 1:
    
        print('\nEscolha a aplicação que deseja utilizar!\n')
        print('Insira "1" para abrir a Calculadora')
        print('Insira "2" para abrir o Chat Bot')
        print('Insira "3" para abrir o Tic-Tac-Toe\n')
        print('Insira qualquer outra resposta para voltar ao menu anterior\n')

        print('Inseriu:')
        answer = input()

        if answer == '1':
            calculadora()
        if answer == '2':
            chatbot()
        if answer == '3':
            tictactoe()
        else:
            return



#Função que permite ao utilizador dar log in e escolher uma aplicação

def logar():

    print('Insira o seu nome de utilizador\n')
    print('Inseriu:')
    nick = input()

    print('\nInsira a sua password\n')
    print('Inseriu:')
    passw = input()

    x = verificadora(nick, passw, 1)

    if (x == 0 or x == 2):

        while x == 0 or x == 2:

            if (x == 2):
                print('\nEsse username não existe\n')
                return ''

            if x == 0:
                print('\nPassword errada\n')
                
            print('Deseja mudar de utilizador? Indique "1" caso deseje, ou "2" caso queira inserir de novo a password. Indique "3" caso queira sair\n')
            print('Inseriu:')
            yn = input()

            if yn == '3':
                return ''

            if yn == '1':

                print('Insira o seu nome de utilizador\n')
                print('Inseriu:')
                nick = input()

                print('Insira a sua password\n')
                print('Inseriu:')
                passw = input()

            if yn == '2':
                print('Insira a sua password\n')
                print('Inseriu:')
                passw = input()

            x = verificadora(nick, passw, 1)

    print('\nLogin efetuado com sucesso!\n')

    while 1:

        print('\nO que deseja fazer?\n')
        print('1 - Mudar de Password \n2 - Fazer Logout \n3 - Escolher uma aplicação\n\n')

        print('Inseriu:')
        answer = input()

        if answer == '1':
            passw = borracha(nick, passw)
        elif answer == '2':
            print('A voltar ao menu de login')
            return()
        elif answer == '3':
            menuapps()
        else:
            print('Resposta inválida')



def main():

    while 1: 
        print('\nComo deseja proceder:\n\n1 - Login\n2 - Registar\n3 - Sair\n')
        print('Inseriu:')
        opt = input()

        if opt=='3':
            print('\nA sair!\n')
            exit()
        elif opt=='2':
            print('\nEspere um momento\n')
            registar()
        elif opt == '1':
            print('\nEspere um momento\n')
            logar()


main()