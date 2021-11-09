from tic_tac import *
import os

def login():

  print("\nLogin")
  username = input("Username->")
  
  file = open("data.txt",'r')
  for line in file:
    lido0 = line.strip().split("-")[0]
    if lido0 == username:
      lido1 = line.strip().split("-")[1]
      password = input ("Password->")
      if lido1 == password:
        print("\nOlá " + lido0 + "! Login efetuado com sucesso")
        return True
      elif lido1 != password:
        print("\nPassword errada")
        return False
  
  print("\nUsername inexistente ->.r para fazer registo de utilizador")
  return False

  file.close()
          

def registar():

  print("\nRegistar utilizador")
  username = input("Username->")

  file = open("data.txt",'r')
  for line in file:
    lido = line.split("-")[0]
    if lido == username:
      print("Esse username ja existe")
      return
  file.close() 
  password = input("Password->")

  file = open("data.txt", 'a+')
  file.write(username)
  file.write("-")
  file.write(password)
  file.write("\n")
  file.close()

  print("\nRegisto efetuado com sucesso!")

def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print("\nHackerLogin ->.h para obter ajuda\n")

  estado = 0

  while True:
    user_in = input("->")
    if user_in == '.h':
        print('''
              Para fazer login -----------------> .l
              Para registar um novo utilizador -> .r
              Para sair ------------------------> .q 
              Para jogar, necessario login -----> .j
              ''' )
    elif user_in == '.l':
        estado = login()

    elif user_in == '.r':
        registar()

    elif user_in == '.q':
        break

    elif user_in == '.j':
      if estado:
        jogar()
      else:
        print("\nLogin necessario")

    else:
      print("\nIsso nao existe -_-")

main()

