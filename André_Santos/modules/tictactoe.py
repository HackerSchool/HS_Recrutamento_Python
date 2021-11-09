from os import system
import sys

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
      
    if checkwin(grid):
      clear()
      draw()
      print(f"             '{cp}' GANHOU!")
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
    
  
    
  