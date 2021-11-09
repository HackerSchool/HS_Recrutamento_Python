import os
from time import sleep
from random import randint

def setcolor(a=0, b=0, c=0):
    if a == b == c == 0:
        print("\033[m", end="")
    else:
        font = "\033["
        if(a != 0):
            font += str(a)
        if(b != 0):
            if(font[-1] != "["):
                font += ";"
            font += str(b)
        if(c != 0):
            if(font[-1] != "["):
                font += ";"
            font += str(c)
        font += "m"
        print(font, end="")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wincheck(jogo, modo):
    #coordenadas de verificação do tabuleiro: horizontais, verticais e oblíquas
    pat = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    empty = 0
    for i in range(8):
        if(jogo[i] == 0):
            empty += 1
        if(jogo[pat[i][0]] == jogo[pat[i][1]] == jogo[pat[i][2]] and jogo[pat[i][0]] != 0):
            print_jogo(jogo, win=[pat[i][0], pat[i][1], pat[i][2]])
            
            if(modo - 1):   #modo 2
                if(jogo[pat[i][0]] == 1):
                    print("Jogador 1 ganha!\nClique Enter para sair")
                else:
                    print("Jogador 2 ganha!\nClique Enter para sair")
            else:           #modo 1
                if(jogo[pat[i][0]] == 1):
                    print("Jogador ganha!\nClique Enter para sair")
                else:
                    print("Computador ganha!\nClique Enter para sair")
            a = input("")
            return 1
    
    if(jogo[8] == 0):
        empty += 1

    if(empty == 0):
        print_jogo(jogo)
        print("Empate!\nClique Enter para sair")
        a = input("")
        return 1
    
    #return(continuar: 0; fim: 1)
    return 0

def player_turn(jogo, player, modo):

    if(player == -1 and modo == 1):
        jogo[bot_turn(jogo)] = -1
    else:
        while(True):    #Loop de tratamento e verificação de input
            
            #Pede um input diferente de acordo com player e modo
            coords = input(("Jogador 1: " if (player == 1 and modo == 2) else ("Jogador: " if (player == 1 and modo == 1) else "Jogador 2: "))).strip().split()
            
            if(coords[0] == "sair"):
                return 1
            
            if(len(coords) == 2 and coords[0].isnumeric() and coords[1].isnumeric()):
                
                if(1 <= int(coords[0]) <= 3 and 1 <= int(coords[1]) <= 3):
                    #Cálculo da posição a jogar
                    pos = (int(coords[0]) - 1) * 3 + int(coords[1]) - 1
                    
                    if(jogo[pos] != 0):
                        print("Não é permitido jogar numa posição já preenchida! Tente outra vez.")
                    else:
                        break
                else:
                    print("Jogada fora do tabuleiro! Tente outra vez.")
            else:
                print("Por favor introduza 2 números separados por espaços ou escreva \"sair\" para sair do jogo.")
        
        #Jogada no tabuleiro
        if(player - 1):
            jogo[pos] = -1
        else:
            jogo[pos] = 1
    
    #return(normal: 0; sair: 1)
    return 0

def bot_turn(jogo):
    print("Computador: ", end="")
    possible = []
    for i in range(9):
        if(jogo[i] == 0):
            possible.append(i)
    
    #jogada aleatória dentro das possíveis
    jogada = randint(0, len(possible) - 1)

    sleep(1)
    print((possible[jogada] // 3) + 1, end=" ")
    sleep(0.5)
    print((possible[jogada] % 3) + 1, end="")
    sleep(0.5)
    print("")

    #return jogada do bot
    return possible[jogada]

def gameloop(modo):
    clear()

    jogo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player = 1

    while(True):
        #player no modo 1: 1, 2, 1, 2, etc
        #player no modo 2: 1, -1, 1, -1, etc
        if(modo - 1 and player == -1):
            #específico do modo 2
            if(player_turn(jogo, 2, modo)):
                return 1
        else:
            if(player_turn(jogo, player, modo)):
                return 1
        
        #Ver se alguém ganhou
        if(wincheck(jogo, modo)):
            break
        else:
            print_jogo(jogo)
        
        #mudança de jogador
        player *= -1
        

    #return(normal: 0; sair: 1)
    return 0

def print_jogo(jogo, win = [0, 0, 0]):
    clear()
    print("")
    if(win[0] == win[1]):
        for l in range(3):
            for c in range(3):
                pos = l * 3 + c
                if(jogo[pos] == 0):
                    print("  ", end="")
                elif(jogo[pos] == 1):
                    print("X ", end="")
                else:
                    print("O ", end="")
            print("")
    else:
        for l in range(3):
            for c in range(3):
                pos = l * 3 + c
                if(jogo[pos] == 0):
                    print("  ", end="")
                elif(jogo[pos] == 1):
                    if(pos in win):
                        setcolor(c=42)
                    print("X ", end="")
                else:
                    if(pos in win):
                        setcolor(c=42)
                    print("O ", end="")
                setcolor(c=40)
            print("")

    return

def rules():
    clear()
    print('''====Regras do Jogo do Galo====
    
    Objetivo:
    O objetivo é ser o primeiro a construir uma linha com 3 peças iguais, que podem ser X ou O.
    
    Regras:
    Os dois jogadores colocam, alternadamente, as suas peças de forma a construirem uma linha com 3 peças iguais num tabuleiro 3 × 3.
    
    Para colocar uma peça no tabuleiro, cada jogador deverá escrever 2 números separados por espaços: o primeiro é a linha, entre 1 e 3, em que quer jogar; o segundo é a coluna, entre 1 e 3, em que quer jogar.
    Exemplo: 2 3
    
    A linha de peças iguais pode ser vertical, horizontal ou oblíqua.
    
    Dicas:
    O jogador deve jogar tendo em conta as seguintes prioridades:
    - Ganhar, completando a linha.
    - Bloquear para impedir que o adversário complete a sua linha.
    - Bloquear jogadas que proporcionem ao adversário mais do que uma posição de vantagem.
    - Jogar no centro.
    - Jogar no canto oposto ao do adversário.
    - Jogar no canto vazio.
    - Jogar no lado vazio.''')
    a = input("Clique Enter para voltar atrás\n")

def main(log, user):
    while(True):    
        clear()
        print("\nJogo do Galo")
        print("Escolha o modo de jogo: \n[1] Singleplayer (Jogador vs Computador)\n[2] Multiplayer (Jogador vs Jogador)\n[3] Regras\n[4] Sair do jogo")
        modo = input("> ").strip()

        if(modo == "1" or modo == "2"):
            gameloop(int(modo))
        elif(modo == "3"):
            clear()
            rules()
        else:
            break
    clear()




