from os import system
import sys
import random

def clear():
  if sys.platform.startswith("linux"):
    system("clear")
  else:
    system("cls")


grid = [" " for _ in range(10)]

def draw():
  print(f"""\n
      {grid[1]} │ {grid[2]} │ {grid[3]}        1 │ 2 │ 3 
     ───┼───┼───      ───┼───┼───       
      {grid[4]} │ {grid[5]} │ {grid[6]}  ====  4 │ 5 │ 6
     ───┼───┼───      ───┼───┼───
      {grid[7]} │ {grid[8]} │ {grid[9]}        7 │ 8 │ 9 
      \n""")

def play(cp):
  while True:
    clear()
    print(f"\n      É a tua vez de jogar!, {cp}!")
    draw()
    #SE FOR O HUMANO
    if cp == "X":
        p = int(input("       Escolhe uma posicao (1-9): "))
        while True:
          if p > 0 and p < 10:
            if grid[p] == " ":
                  grid[p] = cp
                  break
            else:
                  p = int(input(f"   Essa posicao esta ocupada, tente novamente (1-9): "))
          else:
              p =  int(input("   Input invalido (1-9): "))
    else:
      #JOGADA DA AI
      grid[aiplay()] = "O"
      
    if checkwin(grid):
      clear()
      draw()
      if cp == "X":
          print(f"             GJ! GANHASTE!")
      else:
          print(f"        A JUDY GANHOU, BOA TENTATIVA.")
      input("\n\n    Clica no Espaço para reeniciar")
      break
    else:
      if grid.count(" ") == 1:
          clear()
          draw()
          print("             ISTO É UM EMPATE!")
          input("\n\n    Clica no Espaço para reeniciar")
          break
    cp = flip(cp)
    

def checkwin(grid):
  #HORIZONTAIS
  if grid[1] != " ":
    if grid[1] == grid[2] == grid[3]:
      return True
  if grid[4] != " ":
    if grid[4] == grid[5] == grid[6]:
      return True
  if grid[7] != " ":
    if grid[7] == grid[8] == grid[9]:
      return True
   
  #VERTICAIS
  if grid[1] != " ":
    if grid[1] == grid[4] == grid[7]:
      return True
  if grid[2] != " ":
    if grid[2] == grid[5] == grid[8]:
      return True
  if grid[3] != " ":
    if grid[3] == grid[6] == grid[9]:
      return True

  #DIAGONAIS
  if grid[1] != " ":
    if grid[1] == grid[5] == grid[9]:
      return True
  if grid[7] != " ":
    if grid[7] == grid[5] == grid[3]:
      return True

def flip(cp):
    if cp == "X":
        cp = "O"
    else:
        cp = "X"

    return cp
        
def aiplay():
    move = 0
    
    #CALCULAR AS JOGADAS POSSIVEIS
    possibleMoves = [x for x, letter in enumerate(grid) if letter == " " and x != 0]
    
    #CALCULAR OS CANTOS DISPONIVEIS
    openCorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            openCorners.append(i)
            
    #CALCULAR OS LADOS DISPONIVEIS
    openEdges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            openEdges.append(i)
            
    #SE HOUVER UMA JOGADA ++ ENTÃO ESCOLHE-LA
    #SE HOUVER UMA JOGADA -- ENTÃO ESCOLHE-LA
    for let in ["O", "X"]:
        for i in possibleMoves:
            gridCopy = grid[:]
            gridCopy[i] = let
            if checkwin(gridCopy):
                move = i
                return move
            
    #VERIFICAR SE EXISTE CANTOS E ESCOLHER UM ALEATORIO
    if len(openCorners) > 0:
        move = random.choice(openCorners)
        return move
    
    #SE O DO MEIO ESTIVER DISPONIVEL ESCOLHE-LO
    if 5 in possibleMoves:
        move = 5
        return move
     
    #VERIFICAR SE EXISTE LADOS E ESCOLHER UM ALEATORIO
    if len(openEdges) > 0:
        move = random.choice(openEdges)
        return move
     
  
def main(): 
  while True:
    clear()
    playingFirst = input("\n   QUEM VAI JOGAR PRIMEIRO? (00 para sair)\n >>> ").upper()
    if playingFirst == "00":
      break
    elif playingFirst == "X":
        cp = "X"
    else:
        cp = "O"
    play(cp)
    
  
    
  