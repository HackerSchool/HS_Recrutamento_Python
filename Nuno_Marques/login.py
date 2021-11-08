# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:50:46 2021

@author: nuno_
"""


def register():
    #Função que abre o ficheiro, pesquisa se o utilizador já existe e se não existe adiciona ao ficheiro o utilizador, pass
    # e score para o tic-tac-toe. Foi usado um ponto no final porque em comparações o último elemento tem sempre +1 de size.
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    score='0'
    with open('passwords.txt','r+') as registry:
        for line in registry:
            data=line.split(' , ')
            if username==data[0]:
                print("")
                print("There is already an account under that username, try again.")
                return 
            else:
                pass
        registry.write(username + ' , ' + password + ' , ' + score + ' , ' + '.' + '\n')
        print("")
        print("Account sucessfully registered!")
                


def login(username,password):
    #Função que abre o ficheiro, e pesquisa se existe um utilizador com o username e depois se a password corresponde.
    #Aqui uso bool para futuramente usar no menu login.
    with open('passwords.txt','r') as registry:
        for line in registry:
            data=line.split(' , ')
            if username==data[0]:
                if password==data[1]:
                    print("")
                    print("You have sucessfully logon.")
                    return True
                else:
                    print("")
                    print("Wrong password, try again.")
                    return False
            else:
                pass
        print("This account is not present in the registry.")
        return False


def change_score(username):
    #Função que abre o ficheiro e pesquisa o utilizador e adiciona 1 ao score.
    registry = open("passwords.txt",'r') 
    newfile=""
    for line in registry:
        data=line.split(' , ')
        if username==data[0]:
            password=data[1]
            newscoreint=int(data[2])+1
            newscore=str(newscoreint)
            changes= username + ' , ' + password + ' , ' + newscore + ' , ' + '.'
            newfile= newfile + changes +'\n'
        else:
            newfile= newfile + line 
    registry.close()
    registry= open("passwords.txt",'w')
    registry.write(newfile)
    registry.close()

def see_score(username):
    #Função que abre o ficheiro, pesquisa o utilizador e mostra o score.
    #Como um precedente ao uso esta função é um login com bool True não é necessário ter algo caso o username não existe.
    with open('passwords.txt','r') as registry:
        for line in registry:
            data=line.split(' , ')
            if username==data[0]:
                print(username + " score is " + data[2])
                return
            else:
                pass

def change_pass(username,password):
    #Função que abre o ficheiro, pesquisa o utilizador e muda a password
    registry = open("passwords.txt",'r')    
    newfile= ""
    for line in registry:
        data=line.split(' , ')
        if username==data[0]:
            if password==data[1]:
                score=data[2]
                newpass=input("Enter your new password: ")
                changes=  username + ' , ' + newpass +  ' , ' + score + ' , ' +'.'
                newfile= newfile + changes + '\n'
            else:
                newfile= newfile + line 
        else:
             newfile= newfile + line         
    registry.close()
    registry= open("passwords.txt",'w')
    registry.write(newfile)
    registry.close()

