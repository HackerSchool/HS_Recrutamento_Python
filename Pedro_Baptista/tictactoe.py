#Função que imprime o quadro, que é um array com 9 posições

def impressora2d(board):

    print('\n')
    print(board[0] ,'|', board[1], '|', board[2])
    print('---------')
    print(board[3] ,'|', board[4], '|', board[5])
    print('---------')
    print(board[6] ,'|', board[7], '|', board[8], '\n')

#Função que verifica as 8 linhas de vitória possíveis

def verificadora(board):
    
    if board[0] == board[1] and board[1] == board[2]:
        return board[0]
    if board[3] == board[4] and board[4] == board[5]:
        return board[3]
    if board[6] == board[7] and board[7] == board[8]:
        return board[6]

    if board[0] == board[3] and board[3] == board[6]:
        return board[0]
    if board[1] == board[4] and board[4] == board[7]:
        return board[1]
    if board[2] == board[5] and board[5] == board[8]:
        return board[2]
    
    if board[0] == board[4] and board[4] == board[8]:
        return board[0]
    if board[2] == board[4] and board[4] == board[6]:
        return board[2]

    return '0'


#Função cíclica, joga o primeiro jogador, chama a impressora2d e a verificadora, depois joga o segundo jogador
#e vai-se repetindo até haver vencedor ou até ao empate. Caso o user deseje poderá jogar novamente

def tictactoe():
    print("\nTic-Tac-Toe inicializado!\n")
    modo = input('Indique o modo que deseja jogar:\n5: Jogo no terminal de dois jogadores\n7: Jogo no terminal com AI aleatório\n')

    while 1:
        if modo == '5':
            print("\nPara indicar a posição em que deseja jogar, indique o número da casa desejada. Exemplo: 5\n")

            print('0','|', '1', '|', '2')
            print('---------')
            print('3' ,'|', '4', '|', '5')
            print('---------')
            print('6' ,'|', '7', '|', '8', '\n')

            print("O primeiro jogador utilizará o X, o segundo a O\n")

            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            jogadas = 0


            while 1:
                p1 = input('Turno do primeiro jogador\n')
                try:
                    p1 = int(p1)
                except ValueError:
                    print(':( Segue as regras!\n')
                    return

                if p1 > 8 or p1 < 0:
                    print(':( Segue as regras!\n')
                    return

                n = '0'
                while n == '0':
                    if board[p1] == ' ':
                        board[p1] = 'X'
                        n = '1'
                        jogadas += 1
                    else:
                        print('Essa posição é inválida!\n')
                        p1 = input('Insira outra posição\n')
                        p1 = int(p1)


                impressora2d(board)
                w1 = verificadora(board)

                if w1 == 'X':
                    print('O primeiro jogador ganhou!\n')
                    c = input('Deseja sair? Indique "1" caso o deseje, qualquer outra resposta caso deseje continuar\n')
                    if c == '1':
                        return
                    break

                if jogadas == 9:
                    print('Empate!\n')
                    c = input('Deseja sair? Indique "1" caso o deseje, qualquer outra resposta caso deseje continuar\n')
                    if c == '1':
                        return
                    break


                p2 = input('Turno do segundo jogador\n')
                try:
                    p2 = int(p2)
                except ValueError:
                    print(':( Segue as regras!\n')
                    return

                if p2 > 8 or p2 < 0:
                    print(':( Segue as regras!\n')
                    return
                
                n = '0'
                while n == '0':
                    if board[p2]== ' ':
                        board[p2] = 'O'
                        n = '1'
                        jogadas+=1
                    else:
                        print('Essa posição é inválida!\n')
                        p2 = input('Insira outra posição\n')
                        p2 = int(p2)


                impressora2d(board)
                w2 = verificadora(board)

                if w2 == 'O':
                    print('O segundo jogador ganhou!')
                    c = input('Deseja sair? Indique "1" caso o deseje, qualquer outra resposta caso deseje continuar\n')
                    if c == '1':
                        return
                    break
        
        i = '1'
        while modo == '7':
            while i == '1':
                tictactoerand()
                i = input('Deseja jogar outra vez? Indique 1 se sim, qualquer resposta caso contrário\n')
            return()

#Nesta função o segundo jogador é um bot que vai mandando posições ao calhas até que uma seja válida

def tictactoerand():
    import random

    print("\nPara indicar a posição em que deseja jogar, indique o número da casa desejada. Exemplo: 5\n")

    print('0','|', '1', '|', '2')
    print('---------')
    print('3' ,'|', '4', '|', '5')
    print('---------')
    print('6' ,'|', '7', '|', '8', '\n')

    print("O primeiro jogador utilizará o X, o bot a O\n")

    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    jogadas = 0


    while 1:
        p1 = input('Turno do primeiro jogador\n')
        try:
            p1 = int(p1)
        except ValueError:
            print(':( Segue as regras!\n')
            return

        if p1 > 8 or p1 < 0:
            print(':( Segue as regras!\n')
            return

        n = '0'
        while n == '0':
            if board[p1] == ' ':
                board[p1] = 'X'
                n = '1'
                jogadas += 1
            else:
                print('Essa posição é inválida!\n')
                p1 = input('Insira outra posição\n')
                p1 = int(p1)


        impressora2d(board)
        w1 = verificadora(board)

        if w1 == 'X':
            print('O primeiro jogador ganhou!\n')
            return


        if jogadas == 9:
            print('Empate!\n')
            return


        print('Turno do bot\n')
        p2 = random.randint(0,9)

        n = '0'
        while n == '0':
            if board[p2]== ' ':
                board[p2] = 'O'
                n = '1'
                jogadas+=1
            else:
                p2 = random.randint(0,9)

        impressora2d(board)
        w2 = verificadora(board)

        if w2 == 'O':
            print('O bot ganhou!')
            return

    