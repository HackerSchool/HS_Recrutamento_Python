# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 19:21:30 2021

@author: User
"""

from random import randrange

class TicTacToe():
    def __init__(self):
        #self.board = [[' ']*3]*3
        self.board = [[' ']*3, [' ']*3, [' ']*3]
        
        self.p1 = 0 # representado por 0
        self.p2 = 0 # representado por 1
        self.ai = 0 # representado por 1
        
        
    def print_board(self):
        # mostra o tabuleiro
        print('-------------')
        for i in range(3):
            print('|', 0+i*3, '|', 1+i*3, '|', 2+i*3, '|')
            print('-------------')
            
    def print_game(self):
        #mostra as posições da tabuleira
        print('-------------')
        for line in self.board:
            print('|', line[0], '|', line[1], '|', line[2], '|')
            print('-------------')
            
    def print_scores(self, typ = ''):
        # mostra os resultados do jogo
        if typ == 'ai':
            print('AI: ', self.ai)
            print('Player 1: ', self.p1)
        else:
            print('Player 1: ', self.p1)
            print('Player 2: ', self.p2)
        
    def clear_scores(self):
        # mete os resultados a 0
        self.p1 = 0
        self.p2 = 0
        self.ai = 0
        
    def clear_game(self):
        # limpa o campo
        self.board = [[' ']*3, [' ']*3, [' ']*3]
            
    def is_empty(self,x,y):
        # verifica se uma certa posição está ocupada
        if not (0<=x<=2 and 0<=y<=2): return False
        return self.board[x][y] == ' '
    
    def replace(self,player, x,y):
        # se um certo lugfar está vazio ele substitui
        if self.is_empty(x,y):
            #print(self.board[0][1])
            self.board[x][y] = 'X'*(player==0) + 'O'*(player==1)
        # return sobre o jogo já acabou ou não
        return self.won()
        
    def won(self):
        #verifica se o jogo já acabou
        
        #linhas
        for line in self.board:
            if ' ' != line[0]==line[1]==line[2]:
                return True
        # colunas
        for i in range(3):
            if ' ' != self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        #diagonais
        if ' ' !=self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if ' ' != self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False
        
    def s_play1v1(self, not_start = 1):
        #jogo 1v1
        self.print_board()
        player= not_start
        for i in range(9):
            player = (player == 0)
            p = int(input()) #possivel posição
            while not self.is_empty(p//3, p%3):
                # se posicão for inválida continuar até ser válida
                print('Lugar já preenchido ou número inválido')
                p = int(input())
            f = self.replace(player, p//3, p%3)
            self.print_game()
            if f: break
        
        #update dos scores
        if f:
            print(f'O vencedor é o player {player+1}'  )
            self.p1 += player==0
            self.p2 += player == 1
        else:
            print('Empate')
            
        self.print_scores()
        self.clear_game()
        return player
    
    def m_play1v1(self, to_start = 0):
        #multiplos jogo 1v1
        a = 0
        while a != 'q':
            to_start = to_start==0
            self.s_play1v1(to_start)
            a = input('Continuar? (q para sair)')
        self.clear_scores()
        
        
    def s_play_ai(self, player):
        # jogo contra random ai
        self.print_board()
        for i in range(9):
            if player == 0:
                p = int(input())
                while not self.is_empty(p//3, p%3):
                    print('Lugar já preenchido ou número inválido')
                    p = int(input())
                player = 1
            else:
                p = randrange(0, 9)
                while not self.is_empty(p//3, p%3):
                    #print('Lugar já preenchido')
                    p = randrange(0, 9)
                player = 0
            f = self.replace(player==0, p//3, p%3)
            self.print_game()
            if f: break
        
        #update dos scores
        if not f:
            print('Empate')
        elif player == 0:
            print('O vencedor é o AI')
            self.ai += 1
        else:
            print('O vencedor é o player 1')
            self.p1 += 1
        
        self.print_scores('ai')
        self.clear_game()
        return player
                
    def m_play_ai(self, not_start = 1):
        # multiplos jogos contra random ai
        a = 0
        while a != 'q':
            not_start = not_start==0
            self.s_play_ai(not_start)
            a = input('Continuar? (q para sair)')
        self.clear_scores()
        
    
    def s_play_ai2(self, player = 0):
        # jogo contra ai
        self.print_board()
        for i in range(9):
            if player == 0:
                p = int(input())
                while not self.is_empty(p//3, p%3):
                    print('Lugar já preenchido ou número inválido')
                    p = int(input())
                player = 1
            else:
                p = self.clever_ai()
                while not self.is_empty(p//3, p%3):
                    #print('Lugar já preenchido')
                    p = randrange(0, 9)
                player = 0
            f = self.replace(player==0, p//3, p%3)
            self.print_game()
            if f: break
        
        #update dos scores
        if not f:
            print('Empate')
        elif player == 0:
            print('O vencedor é o AI')
            self.ai += 1
        else:
            print('O vencedor é o player 1')
            self.p1 += 1
        
        self.print_scores('ai')
        self.clear_game()
        return player
    
    def m_play_ai2(self, not_start = 1):
        # multiplos jogos contra ai
        a = 0
        while a != 'q':
            not_start = not_start==0
            self.s_play_ai2(not_start)
            a = input('Continuar? (q para sair)')
        self.clear_scores()
    
    def clever_ai(self):
        #define as jogadas do ai player não random
        
        # jogadas predefinidas
        if self.board == [['X', ' ', ' '],[' ', ' ', ' '], [' ', ' ', ' ']] or \
            self.board == [[' ', ' ', 'X'],[' ', ' ', ' '], [' ', ' ', ' ']] or \
                self.board == [[' ', ' ', ' '],[' ', ' ', ' '], ['X', ' ', ' ']] or \
                    self.board == [[' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', 'X']]:
                        return 4
        elif self.board == [['X', ' ', ' '],[' ', 'O', ' '], [' ', ' ', 'X']] or \
            self.board == [[' ', ' ', 'X'],[' ', 'O', ' '], ['X', ' ', ' ']]:
                return [1,3,5,7][randrange(0,4)]
        elif self.board == [[' ', ' ', ' '],[' ', 'X', ' '], [' ', ' ', ' ']]:
            return [0,2,6,8][randrange(0,4)]
        
        #estado do campo
        ls = [[0,0],[0,0],[0,0]]  #[player1;ai]  #linhas
        cs = [[0,0],[0,0],[0,0]]  #colunas
        for i in range(9):
            place = self.board[i//3][i%3]
            if place == 'X':
                ls[i//3][0]+=1
                cs[i%3][0]+=1
            elif place == 'O':
                ls[i//3][1]+=1
                cs[i%3][1]+=1
                
        ds = [[0,0],[0,0]]  #diagonais
        for i in range(3):
            place = self.board[i][i]
            if place == 'X':
                ds[0][0]+=1
            elif place == 'O':
                ds[0][1]+=1
            
            place = self.board[i][~i]
            if place == 'X':
                ds[1][0]+=1
            elif place == 'O':
                ds[1][1]+=1
                

        # verificar se consegue ganhar
        for l in range(3): #linhas
            if  ls[l][0]==0 and ls[l][1]==2:
                for i in range(3):
                    if self.is_empty(l, i): return l*3+i
        for c in range(3): #colunas
            if  cs[c][0]==0 and cs[c][1]==2:
                for i in range(3):
                    if self.is_empty(i, c): return i*3+c
        if (ds[0][0]==0 and ds[0][1]==2): #diagonal
            if self.is_empty(0, 0): return 0
            elif self.is_empty(1, 1): return 4
            elif self.is_empty(2, 2): return 8
        if (ds[1][0]==0 and ds[1][1]==2): #diagonal
            if self.is_empty(0, 2): return 2
            elif self.is_empty(1, 1): return 4
            elif self.is_empty(2, 0): return 6
            
        # verificar se consegue perder
        for l in range(3):  #linhas
            if ls[l][0]==2 and ls[l][1]==0:
                for i in range(3):
                    if self.is_empty(l, i): return l*3+i
        for c in range(3): #colunas
            if cs[c][0]==2 and cs[c][1]==0:
                for i in range(3):
                    if self.is_empty(i, c): return i*3+c
        if (ds[0][0]==2 and ds[0][1]==0): #diagonal
            if self.is_empty(0, 0): return 0
            elif self.is_empty(1, 1): return 4
            elif self.is_empty(2, 2): return 8
        if (ds[1][0]==2 and ds[1][1]==0): #diagonal
            if self.is_empty(0, 2): return 2
            elif self.is_empty(1, 1): return 4
            elif self.is_empty(2, 0): return 6
        
        
        # construir interest matrix
        # avalia a linha. a coluna e a diagonal de cada posição
        # cada posição com o mesmo objeto vale 3 pontos e com o ponto adversario vale 1, os restantes valem 0
        interest = [[0]*3, [0]*3, [0]*3]
        #linhas e colunas
        for l in range(3):
            for c in range(3):
                if ls[l][0]>0 and ls[l][1]>0:
                    pass
                elif self.is_empty(l, c):
                    interest[l][c] += (ls[l][0]>0) + (ls[l][1]>0)*3
                if cs[c][0]>0 and cs[c][1]>0:
                    pass
                elif self.is_empty(l, c):
                    interest[l][c] += (cs[c][0]>0) + (cs[c][1]>0)*3
        #diagonais
        for i in range(2):
            print(1)
            if ds[i][0]>0 and ds[i][1]>0:
                print(2)
                pass
            else:
                print(3)
                for j in range(3):
                    if i == 0 and self.is_empty(j, 2-j):
                        interest[j][~j] += (ds[i][0]>0) + (ds[i][1]>0)*3
                    elif i == 1 and self.is_empty(2-j, j):
                        interest[~j][j] += (ds[i][0]>0) + (ds[i][1]>0)*3
        
        max_ = [-1,-1] #[posição no campo, valor da interest matrix]
        
        for i in range(9):
            if interest[i//3][i%3]>max_[1]:
                max_ = [i,interest[i//3][i%3]]
                
        return max_[0]
        
        
        return randrange(0, 9)
    
    def ai_vs_ai(self, player = 0):
        #jogo ai vs ai
        self.print_board()
        for i in range(9):
            if player == 0:
                p = self.clever_ai()
                while not self.is_empty(p//3, p%3):
                    #print('Lugar já preenchido')
                    p = randrange(0, 9)
                player = 1
            else:
                p = self.clever_ai()
                while not self.is_empty(p//3, p%3):
                    #print('Lugar já preenchido')
                    p = randrange(0, 9)
                player = 0
            f = self.replace(player==0, p//3, p%3)
            self.print_game()
            if f: break
        
        if not f:
            print('Empate')
        elif player == 0:
            print('O vencedor é o AI')
            self.ai += 1
        else:
            print('O vencedor é o player 1')
            self.p1 += 1
        
        self.print_scores('ai')
        self.clear_game()
        return f
    
    def m_ai_vs_ai(self, not_start = 1):
       # 1000 jogos entre ais para ver se é possivel perder; o loop para caso isso aconteça
        for i in range(1000):
            print(i)
            not_start = not_start==0
            f = self.ai_vs_ai(not_start)
            if f:break
            print('----------------------------')

            
        
                    
    
#game = TicTacToe()


def main_ttt():
    game = TicTacToe()
    print("Bem-vindo ao Tic-Tac_Toe\n")
    while True:
        print('''\nEscolhe a tua opção:
              1 - 1v1 com outra pessoa
              2 - Jogo contra AI aleatória
              3 - Jogo contra AI inteligente
              q - Sair
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            game.m_play1v1()
        elif opcao == '2':
            game.m_play_ai()
        elif opcao == '3':
            game.m_play_ai2()
        elif opcao == 'a':
            game.m_ai_vs_ai()
        elif opcao == 'q':
            print("A sair")
            break
        else:
            print("Opcao não válida")
            
#main_ttt()

    
    