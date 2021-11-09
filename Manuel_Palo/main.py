"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        HackerSchool - Recrutamento
        Projeto 1 - "Login com Apps!"

        Nome: Manuel Falcão Cardoso Palo
        Número do IST: 93120
        Entrega: 8 de Novembro (2ªfeira)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

import calculator
import chatbot
import tictactoe


def app_select(in_username, in_password):
        print("\n-------------------------\n|                       |\n|    · App Select ·     |\n|                       |\n|  1 - Calculator       |\n|                       |\n|  2 - ChatBot          |\n|                       |\n|  3 - Tic-Tac-Toe      |\n|                       |\n|  4 - Login Menu       |\n|                       |\n-------------------------\n")
        option = input("Type the option's number: ")       

        if option == '1':
                print("\nWelcome to the Calculator!")
                calculator.calculator()
                return(in_username, in_password)
        elif option == '2':
                print("\nWelcome to the ChatBot!")
                chatbot.chatbot()
                return(in_username, in_password)
        elif option == '3':
                print("\nWelcome to Tic-Tac-Toe!")
                tictactoe.tictactoe()
                return(in_username, in_password)
        elif option == '4':
                return(in_username, in_password)
        else:
                print("\n<ERROR> Unknown Option\n")
                app_select()



def change_password(in_username, in_password):
        print("\n· Change Password ·\n")

        new_password = input("New Password: ")
        if new_password == in_password:
                print("\nX - Same Password\nPlease try again!\n")
                change_password(in_username, in_password)

        # Guarda um array de linhas
        fp = open("users.txt", "r")
        fp.seek(0,0)
        lines = fp.readlines()
        fp.close()

        # Escreve as linhas do array e altera a linha pretendida
        fp = open("users.txt", "w")
        fp.seek(0,0)
        for line in lines:
                if in_username == line.split(' - ')[0]:
                        aux1 = '- ' + in_password
                        aux2 = '- ' + new_password
                        line = line.replace(aux1,aux2)
                        print("\n✓ - Password Changed\n")
                fp.write(line)
        fp.close()

        login()
        


def login_menu(in_username, in_password):
        print("\n-------------------------\n|                       |\n|    · Login Menu ·     |\n|                       |\n|  1 - Select App       |\n|                       |\n|  2 - Change Password  |\n|                       |\n|  3 - Logout           |\n|                       |\n-------------------------\n")
        option = input("Type the option's number: ")       

        if option == '1':
                app_select(in_username, in_password)
                login_menu(in_username, in_password)
        elif option == '2':
                change_password(in_username, in_password)
        elif option == '3':
                print("\nYou have logged out successfully!")
        else:
                print("\n<ERROR> Unknown Option\n")
                login_menu(in_username, in_password)
        return



def register():
        print("\n· Register ·\n")

        reg_username = input("New Username: ")
        fp = open("users.txt", "a+")
        fp.seek(0,0)
        
        # Verifica se o Username se encontra livre
        for line in fp:
                username = line.split(' - ')[0]
                if reg_username == username:
                        print("\nX - Username already registered\n")
                        reg_username = input("Username: ")
                        fp.seek(0,0)
        reg_password = input("New Password: ")
        fp.seek(0,0)

        # Regista o Username
        fp.write('\n' + reg_username + ' - ' + reg_password)
        print("\n✓ - New user registered\n")

        fp.close()

        login()
        return



def login():
        print("\n· Login ·\n")

        fp = open("users.txt", "r")
        fp.seek(0,0)

        # Verifica se o ficheiro está vazio, lendo o primeiro caractere
        first_char = fp.read(1)
        if first_char == '':
                print("\n<EMPTY FILE> No Users Registered\nPlease Register!\n")
                register()
        fp.seek(0,0)

        # Obtém o número de linhas do ficheiro '.txt'
        aux = fp.readlines()
        n_lines = len(aux)
        n = 0
        fp.seek(0,0)

        in_username = input("Username: ")
        in_password = input("Password: ")

        # Verifica a existência do Username e a respetiva Password
        for line in fp:
                username = line.split(' - ')[0]
                password = line.split(' - ')[1]
                password = password.strip()             # para remover o '\n' de cada linha !!!    [remove whitespaces de trás e de frente - geeksforgeeks.org]
                if in_username == username:
                        if in_password == password:
                                print("\n✓ - Logged in")
                                break
                        elif in_password != password:
                                print("\nX - Wrong password\n")
                                in_username = input("Username: ")
                                in_password = input("Password: ")
                                n = 0
                                fp.seek(0,0)
                elif in_username != username:
                        n += 1
                        if n >= n_lines:
                                print("\nX - Username not registered\n")
                                in_username = input("Username: ")
                                in_password = input("Password: ")
                                n = 0
                                fp.seek(0,0)

        fp.close()

        login_menu(in_username, in_password)
        return



def main():
        print("\n-------------------------\n|                       |\n|    · Main Menu ·      |\n|                       |\n|  1 - Login            |\n|                       |\n|  2 - Register         |\n|                       |\n|  3 - Exit             |\n|                       |\n-------------------------\n")
        option = input("Type the option's number: ")       

        if option == '1':
                print("\nLogin selected!")
                login()
                main()
        elif option == '2':
                print("\nRegister selected!")
                register()
                main()
        elif option == '3':
                print("\nSee you next time!\n")
                return
        else:
                print("\n<ERROR> Unknown Option\n")
                main()
        
        return



main()