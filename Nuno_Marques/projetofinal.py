# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:36:30 2021

@author: nuno_
"""
import login
import tictactoe
def login_menu(username,password):
    print('''\nChoose your option:
             1 - App
             2 - Change Password
             3 - Return to Main Menu
             ''')
    option=input("Enter your option: ")
    if option=='1':
        app_menu(username,password)           
    elif option=='2':
        login.change_pass(username,password)
        print("")
        print("Password changed!")
        print("")
        input("Press any key to return to main menu: ")
        return main()
    elif option=='3':
        return main()
    else:
        print("")
        print("There is no such option! Try again.")
        print("")
        return login_menu(username,password)

def app_menu(username,password):
    print("")
    print("The positions on this tic-tac-toe are defined in the square below. First goes 'X' then goes 'O'.")
    print(" ___________")
    print("|   |   |   |")
    print("| 1 | 2 | 3 |")
    print("|___|___|___|")
    print("|   |   |   |")
    print("| 4 | 5 | 6 |")
    print("|___|___|___|")
    print("|   |   |   |")
    print("| 7 | 8 | 9 |")
    print("|___|___|___|")
    
    print('''\nChoose your option:
             1 - Play with RANDOMBOT 3.0
             2 - Play with a Friend 
             3 - Play with HAL 9000
             4 - Check your score
             5 - Exit to Login Menu
             6 - Return to Main Menu''')
    
    option=input("Enter your option: ")
    game=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    if option=='1':
        while tictactoe.check_board(game):
            tictactoe.updateX(game)
            if tictactoe.check_winX(game):
                login.change_score(username)
                tictactoe.display(game)
                print("")
                print("Congratulations " + username + " has won...")
                print("")
                input("Press any key to return to app menu: ")
                return app_menu(username,password)
            else:
                tictactoe.display(game)
            if tictactoe.check_board(game):
                pos=tictactoe.avail_pos(game)
                tictactoe.bot(game,pos)
                if tictactoe.check_winO(game):
                    login.change_score("RANDOMBOT 3.0")
                    tictactoe.display(game)
                    print("")
                    print("You lost to a random generator, unlucky.")
                    print("")
                    input("Press any key to return to app menu: ")
                    return app_menu(username,password)
                else:
                    tictactoe.display(game)
            else:
                pass
        login.change_score("RANDOMBOT 3.0")
        login.change_score(username)
        tictactoe.display(game)
        print("")
        print("It's a Draw! Humanity is doomed...")
        print("")
        input("Press any key to exit: ")
    elif option=='2':  
        while tictactoe.check_board(game):
            #Aqui apenas continua a jogar se pelo menos 1 quadrado tiver vazio.
            tictactoe.updateX(game)
            #Primeiro fazemos o update da board para depois ver se de facto o jogo está ganho ou não.
            if tictactoe.check_winX(game):
                login.change_score(username)
                tictactoe.display(game)
                print("")
                print("Congratulations " + username + " has won!")
                print("")
                input("Press any key to return to app menu: ")
                return app_menu(username,password)
            else:
                tictactoe.display(game)
            if tictactoe.check_board(game):
                #Aqui foi preciso adicionar novamente um check_board porque pedia sempre para introduzir novamente mesmo 
                #com os quadrados completos.
                tictactoe.updateO(game)
                if tictactoe.check_winO(game):
                    login.change_score("Guest")
                    tictactoe.display(game)
                    print("")
                    print("Congratulations Guest has won!")
                    print("")
                    input("Press any key to return to app menu: ")
                    return app_menu(username,password)
                else:
                 tictactoe.display(game)
            else:
                pass
        #Se ninguém tiver ganho quando tiverem todos os quadrados preenchidos então é declarado oficialmente um empate.
        login.change_score(username)
        login.change_score("Guest")
        print ("It's a Draw!")
        print("")
        input("Press any key to exit: ")
        return
    elif option=='3':
       menu_bot(game,username,password)
    elif option== '4':
        print("")
        login.see_score(username)
        print("")
        input("Press any key to return to app menu: ")
        return app_menu(username,password)
        
    elif option== '5': 
        return login_menu(username,password)
    
    elif option=='6':
        return main()
    else:
        print("")
        print("There is no such option! Try again")
        print("")
        return app_menu(username,password)
    
def menu_bot(game,username,password):
    print('''\nChoose your option:
             1 - You start
             2 - Hal starts
             ''')
    option=input("Enter your option: ")
    if option=='1':
        if tictactoe.tartaruga(game)==True:
            login.change_score("HAL 9000")
            input("Press any key to return to app menu: ")
            return app_menu(username,password)
        else:
            login.change_score("HAL 9000")
            login.change_score(username)
            input("Press any key to return to app menu: ")
            return app_menu(username,password)
    elif option=='2':
        if tictactoe.hal9000(game)==True:
            login.change_score("HAL 9000")
            input("Press any key to return to app menu: ")
            return app_menu(username,password)
        else:
            login.change_score("HAL 9000")
            login.change_score(username)
            input("Press any key to return to app menu: ")
            return app_menu(username,password)
    else:
        print("")
        print ("There is no such option!")
        print("")
        return menu_bot(game,username,password)

def main():
    print('''\nChoose your option:
             1 - Register
             2 - Login
             3 - Exit
             ''')
    option=input("Enter your option: ")
    if option=='1':
        login.register()
        return main()
    elif option=='2':
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if login.login(username,password)==True:
           login_menu(username,password)
        else:
            return main()
    elif option=='3':
        print("")
        input("Press any key to exit: ")
        return
    else:
        print("")
        print("There is no such option! Try again")
        print("")
        return main()

main()