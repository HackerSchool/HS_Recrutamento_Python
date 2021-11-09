# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:15:30 2021

@author: luis_
"""
import time 

def tic_tac_toe():
    
    print(chr(27) + "[2J") # Limpa o terminal 
    print("------ Tic-tac-toe -------")
    print("------------------------------------------------------------------------------------------------")
    print("|                                                                                              |")
    print("|     ------  .   ------         ------     /\    ------       ------    /-----\   -----       |")
    print("|        |    |   |                 |      /  \   |               |      |     |   |____       |")
    print("|        |    |   |        ---      |     /----\  |       ---     |      |     |   |           |")
    print("|        |    |   ------            |    /      \ ------          |      \-----/   -----       |")
    print("------------------------------------------------------------------------------------------------")
    
    print("\n")
    print("\n")
    
    print("                                          |      |      ")
    print("                                       1  |  2   |  3   ")
    print("                                          |      |      ")
    print("                                    --------------------")
    print("                                          |      |      ")
    print("                                       4  |  5   |  6   ")
    print("                                          |      |      ")
    print("                                    --------------------")
    print("                                          |      |      ")
    print("                                       7  |  8   |  9   ")
    print("                                          |      |      ")
    
    print("\n")
    print("\n")
    
    
        
    print("Não é permitido repetir espaços alocados ao outro jogador !!")
    
    lista_x = []
    lista_O = []
    
    
    for i in range(5):        # repetir até i = 5 , na realizadade no ultimo turno, o jogador O ja não joga portanto não tem interesse o valor para esse turno do O.
        
        
    
        x = int(input("Jogador X , introduza a posição que pretende (1 a 9): "))
        
        lista_x.append(x)       # adiciona valores de x à lista_x para i até 5
        
        print("\n")
        
        

        O = int(input("Jogador O , introduza a posição que pretende (1 a 9): "))
        
        lista_O.append(O)       # adiciona valores de O à lista_O para i até 5
        
        #time.sleep(2)
        
    print(lista_x)
    print(lista_O)
            
    # Jogadas possiveis para ganhar o jogo
                      
    if 1 in lista_x and 2 in lista_x and 3 in lista_x :
            
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
             
             
    elif 4 in lista_x and 5 in lista_x and 6 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 7 in lista_x and 8 in lista_x and 9 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 1 in lista_x and 4 in lista_x and 7 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
    
    elif 2 in lista_x and 5 in lista_x and 8 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
    
    elif 3 in lista_x and 6 in lista_x and 9 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 1 in lista_x and 5 in lista_x and 9 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 3 in lista_x and 5 in lista_x and 7 in lista_x :
        
        print("----------------------------")        
        print ("Jogador X é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
            
     # para jogador O 
        
    elif 1 in lista_O and 2 in lista_O and 3 in lista_O :
            
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
             
             
    elif 4 in lista_O and 5 in lista_O and 6 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 7 in lista_O and 8 in lista_O and 9 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 1 in lista_O and 4 in lista_O and 7 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)

    elif 2 in lista_O and 5 in lista_O and 8 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)

    elif 3 in lista_O and 6 in lista_O and 9 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 1 in lista_O and 5 in lista_O and 9 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
        
    elif 3 in lista_O and 5 in lista_O and 7 in lista_O :
        
        print("----------------------------")        
        print ("Jogador O é vencedor !!! ")
        print("----------------------------") 
        time.sleep(5)
    
    else:
        print("Empatado !!!")
        
        time.sleep(10)
        
        
        
        
        
        
        
        
        
        
        