# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:27:08 2021

@author: nuno_
"""
import random
import copy 
   
def check_game(game,i,j):
    #Função pura e simplesmente auxiliar.
    if game[i][j]==' ':
        return True
    else:
        return False

def avail_pos(game):
    #Função que devolve a lista de posições disponíveis
    avail_pos=[]
    for i in range(3):
        for j in range(3):
            if game[i][j]==' ':
                avail_pos=avail_pos+[[i,j]]
            else:
                pass
    return avail_pos
 
def bot(game,avail_pos):
    #Função que dada as posições disponíveis devolve uma ao-calhas
    pos=random.choice(avail_pos)
    i=pos[0]
    j=pos[1]
    game[i][j]='O'
    return game

def win_optionsX(game):
    #Função que devolve os quadrados nos quais se X jogar ganha o jogo
    fakegame=copy.deepcopy(game)
    available=avail_pos(fakegame)
    win_optionsX=[]
    for pos in available:
        i=pos[0]
        j=pos[1]
        fakegame[i][j]='X'
        if check_winX(fakegame):
            win_optionsX=win_optionsX+[[i,j]]
            fakegame=copy.deepcopy(game)
        else:
            fakegame=copy.deepcopy(game)
    return win_optionsX

def win_optionsO(game):
  #Função que devolve os quadrados nos quais se O jogar ganha o jogo  
  fakegame=copy.deepcopy(game)
  available=avail_pos(fakegame)
  win_optionsO=[]
  for pos in available:
      i=pos[0]
      j=pos[1]
      fakegame[i][j]='O'
      if check_winO(fakegame):
          win_optionsO=win_optionsO+[[i,j]]
          fakegame=copy.deepcopy(game)
      else:
          fakegame=copy.deepcopy(game)
  return win_optionsO

def win_condX(game):
    #Aqui defino wincond como sendo um quadrado em que os 'X' tem duas linhas para ganhar
    fakegame=copy.deepcopy(game)
    available=avail_pos(fakegame)
    win_cond=[]
    for pos in available:
        i=pos[0]
        j=pos[1]
        fakegame[i][j]='X'
        win=win_optionsX(fakegame)
        if len(win)==2:
            win_cond=win_cond+[[i,j]]
            fakegame=copy.deepcopy(game)
        else:
            fakegame=copy.deepcopy(game)
    return win_cond

def win_tryX(game):
    #Aqui tenta encontrar uma de linha para o qual os X's podem ganhar na próxima jogada se nesta colocarem um X em certa posição
    fakegame=copy.deepcopy(game)
    available=avail_pos(fakegame)
    win_try=[]
    for pos in available:
        i=pos[0]
        j=pos[1]
        fakegame[i][j]='X'
        win=win_optionsX(fakegame)
        if len(win)==1:
            win_try=win_try+[[i,j]]
            fakegame=copy.deepcopy(game)
        else:
            fakegame=copy.deepcopy(game)
    return win_try

def win_tryO(game):
    #Aqui tenta encontrar uma de linha para o qual os X's podem ganhar na próxima jogada se nesta colocarem um O em certa posição
    fakegame=copy.deepcopy(game)
    fakegame=copy.deepcopy(game)
    available=avail_pos(fakegame)
    win_try=[]
    for pos in available:
        i=pos[0]
        j=pos[1]
        fakegame[i][j]='O'
        win=win_optionsO(fakegame)
        if len(win)==1:
            win_try=win_try+[[i,j]]
            fakegame=copy.deepcopy(game)
        else:
            fakegame=copy.deepcopy(game)
    return win_try
    

def win_condO(game):
    #Aqui defino wincond como sendo um quadrado em que os 'O' tem duas linhas para ganhar
    fakegame=copy.deepcopy(game)
    available=avail_pos(fakegame)
    win_cond=[]
    for pos in available:
        i=pos[0]
        j=pos[1]
        fakegame[i][j]='O'
        win=win_optionsO(fakegame)
        if len(win)==2:
            win_cond=win_cond+[[i,j]]
            fakegame=copy.deepcopy(game)
        else:
            fakegame=copy.deepcopy(game)
    return win_cond
            
def tartaruga(game):
    #Função que empata o tic-tac-toe ou ganha.
    #É defensivo no sentido em que empata sempre e tenta ganhar sempre acha que em 2 jogadas ganha.
    #Primeiro vê se consegue ganhar na jogada, depois se o oponente ganha na próxima jogada, depois 
    #vê se pode por num quadrado que permite ganhar em 2 linhas, depois impede o X de fazer isto, depois tenta por num 
    #quadrado em que ganha numa linha e depois põe num quadrado que impede X de fazer o mesmo. Por último escolhe 
    #simplesmente ao calhas.
    #Quando não começa no meio põe sempre no meio primeiro. Quando não começa no meio foi também adicionada outra condição que
    #Impede de abusar os cantos para ganhar.
    other_pos=['1','2','3','4','6','7','8','9']
    position=input("Enter your position: ")
    if position=='5':
        updateX_pos(game,position)
        updateO_pos(game,'3')
        display(game)
        while check_board(game):
            position=input("Enter your position: ")
            updateX_pos(game,position)
            if check_board(game):
                if win_optionsO(game)!=[]:
                    win=win_optionsO(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                    print("")
                    print("Hal9000 wins!")
                    return True
                    return
                
                if win_optionsX(game)!=[]:
                    win=win_optionsX(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                
                elif win_condO(game)!=[]:
                    win=win_condO(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                
                elif win_condX(game)!=[]:
                    win=win_condX(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                    
                elif win_tryO(game)!=[]:
                    win=win_tryO(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
                    
                elif win_tryX(game)!=[]:
                    win=win_tryX(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
                else:
                    available=avail_pos(game)
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
            else:
                display(game)
                print("")
                print ("It's a Draw!")
                return False
    elif position in other_pos:
        updateX_pos(game,position)
        updateO_pos(game,'5')
        display(game)
        while check_board(game):
            position=input("Enter your position: ")
            updateX_pos(game,position)
            if check_board(game):
                if win_optionsO(game)!=[]:
                    win=win_optionsO(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                    print("")
                    print("Hal9000 wins!")
                    return True
                
                
                if win_optionsX(game)!=[]:
                    win=win_optionsX(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                
                
                elif len(win_condX(game))==2:
                    #Esta condição foi adicionada para parar os cantos (Visualizar 1->9)
                    win=win_condX(game)
                    available=avail_pos(game)
                    available.remove(win[0])
                    available.remove(win[1])
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
                
                elif win_condO(game)!=[]:
                    win=win_condO(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                
                elif win_condX(game)!=[]:
                    win=win_condX(game)[0]
                    i=win[0]
                    j=win[1]
                    game[i][j]='O'
                    display(game)
                
                elif win_tryO(game)!=[]:
                    win=win_tryO(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
                

                elif win_tryX(game)!=[]:
                    win=win_tryX(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
                else:
                    available=avail_pos(game)
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='O'
                    display(game)
            else:
                display(game)
                print("")
                print ("It's a Draw!")
                return False
        else:
            display(game)
            print("")
            print ("It's a Draw!")
            return False
    else:
        print("")
        print ("There is no such option!")
        return tartaruga(game)
    
            
        
        
       
            
def hal9000(game):
    #Este ou empata ou ganha sempre. É baseado numa combinação de jogo que força sempre o segundo a responder logo é levado a 
    #um jogo já determinado.
    game[2][0]='X'
    print("You are O's")
    display(game)
    position=input("Enter your position: ")
    updateO_pos(game,position)
    if position=='8' or position=='9' or position=='6':
        game[0][0]='X'
        display(game)
        position2=input("Enter your position: ")
        updateO_pos(game,position2)
        if win_optionsX(game)==[]:
            if position=='8' or '9':
                game[0][2]='X'
                display(game)
                position3=input("Enter your position: ")
                updateO_pos(game,position3)
                win=win_optionsX(game)
                pos=random.choice(win)
                i=pos[0]
                j=pos[1]
                game[i][j]='X'
                display(game)
                print("")
                print("HAL 9000 has won!")
                return True
            elif position=='6':
                game[1][1]='X'
                display(game)
                position3=input("Enter your position: ")
                updateO_pos(game,position3)
                win=win_optionsX(game)
                pos=random.choice(win)
                i=pos[0]
                j=pos[1]
                game[i][j]='X'
                display(game)
                print("")
                print("HAL 9000 has won!")
                return True
        else:
            game[1][0]='X'
            display(game)
            print("")
            print("HAL 9000 has won!")
            return True
            
    elif position=='1' or position=='2' or position=='4':
        game[2][2]='X'
        display(game)
        position2=input("Enter your position: ")
        updateO_pos(game,position2)
        if win_optionsX(game)==[]:
            if position=='1' or position=='2':
                game[0][2]='X'
                display(game)
                position3=input("Enter your position: ")
                updateO_pos(game,position3)
                win=win_optionsX(game)
                pos=random.choice(win)
                i=pos[0]
                j=pos[1]
                game[i][j]='X'
                display(game)
                print("")
                print("HAL 9000 has won!")
                return True
            elif position=='4':
                game[1][1]='X'
                display(game)
                position3=input("Enter your position: ")
                updateO_pos(game,position3)
                win=win_optionsX(game)
                pos=random.choice(win)
                i=pos[0]
                j=pos[1]
                game[i][j]='X'
                display(game)
                print("")
                print("HAL 9000 has won")
                return True
        else:
            game[2][1]='X'
            display(game)
            print("")
            print("HAL 9000 has won")
            return True
        
    elif position=='3':
        game[0][0]='X'
        display(game)
        position2=input("Enter your position: ")
        updateO_pos(game,position2)
        if win_optionsX(game)==[]:
            game[2][2]='X'
            display(game)
            position3=input("Enter your position: ")
            updateO_pos(game,position3)
            win=win_optionsX(game)
            pos=random.choice(win)
            i=pos[0]
            j=pos[1]
            game[i][j]='X'
            display(game)
            print("")
            print("HAL 9000 has won!")
            return True
        else:
            win=win_optionsX(game)
            pos=random.choice(win)
            i=pos[0]
            j=pos[1]
            game[i][j]='X'
            display(game)
            print("")
            print("HAL 9000 has won!")
            return True
        
    elif position=='5':
        game[0][0]='X'
        display(game)
        position2=input("Enter your position: ")
        updateO_pos(game,position2)
        if win_optionsX(game)==[]:
            game[1][2]='X'
            display(game)
            position3=input("Enter your position: ")
            updateO_pos(game,position3)
            if position3=='3':
                game[2][1]='X'
                display(game)
                position4=input("Enter your position: ")
                updateO_pos(game,position4)
                if win_optionsX(game)==[]:
                    available=avail_pos(game)
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("It's a Draw!")
                    return False
                else:
                    win=win_optionsX(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("HAL 9000 has won!")
                    return True
            elif position3=='9':
                game[0][1]='X'
                display(game)
                position4=input("Enter your position: ")
                updateO_pos(game,position4)
                if win_optionsX(game)==[]:
                    available=avail_pos(game)
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("It's a Draw!")
                    return False
                else:
                    win=win_optionsX(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("HAL 9000 has won!")
                    return True
                
            elif position3=='2' or position3=='8':
                win=win_optionsO(game)
                pos=random.choice(win)
                i=pos[0]
                j=pos[1]
                game[i][j]='X'
                display(game)
                position4=input("Enter your position: ")
                updateO_pos(game,position4)
                if win_optionsX(game)==[]:
                    available=avail_pos(game)
                    pos=random.choice(available)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("It's a Draw!")
                    return False
                else:
                    win=win_optionsX(game)
                    pos=random.choice(win)
                    i=pos[0]
                    j=pos[1]
                    game[i][j]='X'
                    display(game)
                    print("")
                    print("HAL 9000 has won!")
                    return True
                    
        else:
            game[1][0]='X'
            display(game)
            print("")
            print("HAL 9000 wins!")
            return True
    
def check_board(game):
    #Vê-se o tabuleiro tem pelo menos 1 quadrado vazio.
    for i in range(3):
        for j in range(3):
            if check_game(game,i,j):
                return True
            else:
                pass
    return False
  
def updateX(game):
    #Recebe um input e traduz esse input na lista de listas.
    #Se o input ou já tiver ocupado ou for errado é dada uma chance para o jogador meter outro input correto.
    position=input("Enter the position for X: ")
    if position=='1':
        if check_game(game,0,0):
            game[0][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='2':
        if check_game(game,0,1):
            game[0][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='3': 
        if check_game(game,0,2):
            game[0][2]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='4':
        if check_game(game,1,0):
            game[1][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='5':
        if check_game(game,1,1):
            game[1][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='6':
        if check_game(game,1,2):
            game[1][2]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='7':
        if check_game(game,2,0):
            game[2][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='8':
        if check_game(game,2,1):
            game[2][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    elif position=='9':
        if check_game(game,2,2):
            game[2][2]='X'
            return game
        else:
            print("Position is filled. Try again")
            return updateX(game)
    else:
        print("There is no option!")
        updateX(game)
        
def updateX_pos(game,position):
    #Função feita para conciliar a maneira como os bots foram feitos, faz a mesma que a outra só que com 2 argumentos
    if position=='1':
        if check_game(game,0,0):
            game[0][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='2':
        if check_game(game,0,1):
            game[0][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='3':
        if check_game(game,0,2):
            game[0][2]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='4':
        if check_game(game,1,0):
            game[1][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='5':
        if check_game(game,1,1):
            game[1][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='6':
        if check_game(game,1,2):
            game[1][2]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='7':
        if check_game(game,2,0):
            game[2][0]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='8':
        if check_game(game,2,1):
            game[2][1]='X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    elif position=='9':
        if check_game(game,2,2):
            game[2][2]= 'X'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateX_pos(game,position)
    else:
        print("There is no option!")
        position=input("Enter your position: ")
        updateX_pos(game,position)

def updateO(game):
    #Faz o mesmo que a função indicada acima mas para os 'O's.
    position=input("Enter the position for O: ")
    if position=='1':
        if check_game(game,0,0):
            game[0][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='2':
        if check_game(game,0,1):
            game[0][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='3':
        if check_game(game,0,2):
            game[0][2]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='4':
        if check_game(game,1,0):
            game[1][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='5':
        if check_game(game,1,1):
            game[1][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='6':
        if check_game(game,1,2):
            game[1][2]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='7':
        if check_game(game,2,0):
            game[2][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='8':
        if check_game(game,2,1):
            game[2][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    elif position=='9':
        if check_game(game,2,2):
            game[2][2]= 'O'
            return game
        else:
            print("Position is filled. Try again")
            return updateO(game)
    else:
        print("There is no option!")
        updateO(game)  


def updateO_pos(game,position):
    #Função feita para conciliar a maneira como os bots foram feitos, faz a mesma que a outra só que com 2 argumentos
    if position=='1':
        if check_game(game,0,0):
            game[0][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='2':
        if check_game(game,0,1):
            game[0][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='3':
        if check_game(game,0,2):
            game[0][2]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='4':
        if check_game(game,1,0):
            game[1][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='5':
        if check_game(game,1,1):
            game[1][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='6':
        if check_game(game,1,2):
            game[1][2]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='7':
        if check_game(game,2,0):
            game[2][0]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='8':
        if check_game(game,2,1):
            game[2][1]='O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    elif position=='9':
        if check_game(game,2,2):
            game[2][2]= 'O'
            return game
        else:
            print("Position is filled. Try again")
            position=input("Enter your position: ")
            return updateO_pos(game,position)
    else:
        print("There is no option!")
        position=input("Enter your position: ")
        updateO_pos(game,position)
                   
def check_winX(game):
    #Aqui poderia ter usado um loop para ir buscar as diagonais, mas como vai ter dimensão constante posso simplesmente
    #inicializar logo
    diag1=[game[0][0],game[1][1],game[2][2]]
    diag2=[game[2][0],game[1][1],game[0][2]]
    for i in range(3):
        if game[i]==['X','X','X']:
            return True
        else:
            pass
    if diag1==['X','X','X']:
        return True
    else:
        pass
    if diag2==['X','X','X']:
        return True
    else:
        pass
    for j in range(3):
        col=[]
        for i in range(3):
            col=col+[game[i][j]]
        if col==['X','X','X']:
            return True
        else:
            pass
    return False
                        
def check_winO(game):
    #Mesmo coisa que a função acima só que desta vez verifica se os O's ganharam.
    diag1=[game[0][0],game[1][1],game[2][2]]
    diag2=[game[2][0],game[1][1],game[0][2]]
    for i in range(3):
        if game[i]==['O','O','O']:
            return True
        else:
            pass
    if diag1==['O','O','O']:
        return True
    else:
        pass
    if diag2==['O','O','O']:
        return True
    else:
        pass
    for j in range(3):
        col=[]
        for i in range(3):
            col=col+[game[i][j]]
        if col==['O','O','O']:
            return True
        else:
            pass
    return False     


def display(game):
    #Esta função tal como o nome indica da display ao jogo.
    #Foram usadas letras porque são representam bem o tamanho que os 'X' e os 'O' vão ocupar
    #Porquê um display com prints? Não conseguia parar de pensar na ideia de fazer um 3x3 interativo no terminal.

    a=game[0][0]
    b=game[0][1]
    c=game[0][2]
    d=game[1][0]
    e=game[1][1]
    f=game[1][2]
    g=game[2][0]
    h=game[2][1]
    i=game[2][2]
    print(" ___________")
    print("|   |   |   |")
    print("| "+ a +" |" + " " + b + " |" + " " + c + " |")
    print("|___|___|___|")
    print("|   |   |   |")
    print("| "+ d +" |" + " " + e + " |" + " " + f + " |")
    print("|___|___|___|")
    print("|   |   |   |")
    print("| "+ g +" |" + " " + h + " |" + " " + i + " |")
    print("|___|___|___|")



