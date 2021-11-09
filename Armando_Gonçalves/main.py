from calculadora import *






def mudarpass(user):

  contador =-1
  stop = 0
  password = input("\nInsira a nova password:")
  f2 = open("base_de_dados.txt", 'r+')
  f2.seek(0)
  
  
  for line in f2:
    
     
    if(stop == 0):
      contador += 1
      if(user == line.split()[0]):
        stop = 1                  #pouco eficiente?
    
  
  f2.seek(0)
  copia = f2.readlines()   #solução que eu achei mais intuitiva
  
  copia[contador] = (user + " " + password + "\n")
  
  f2.close()
  f2 = open("base_de_dados.txt", 'w+')
  f2.writelines(copia)
  f2.close()
  return


def menulogin(user):

  resposta1 = ''

  print("\n-> Bem vindo ao menu da aplicação.")

  while(resposta1 != 'L'):

    resposta1 = input("\n\n \
    Iniciar calculadora ------ prima 'I' e enter\n \
    Mudar a password --------- prima 'M' e enter\n \
    Logout ------------------- prima 'L' e enter\n\n").upper()

    if resposta1 == 'I':
      yo()

    elif resposta1 == 'M':
      mudarpass(user)

    elif resposta1 == 'L':
      print("\n-> A desconectar...")
      return

    else:
      print("\n-> Por favor insira apenas 'I', 'M' ou 'L' seguido de enter.")


def autenticar():

  controlo_user=0
  controlo_pass = 0
  linha=0
  b=0
  
  user = input("\nUsername:")
    
    
  file = open("base_de_dados.txt", 'a+')
  file.seek(0)
  for line in file:
    if (user == line.split()[0]):
      password = input("Password:")
      controlo_user = 1
      while(password != line.split()[1]):
        print("\n-> Password errada. Tente novamente.\n")
        password = input("Password:")
        b += 1
        if b>3:
          print("\n-> Errou a password demasiadas vezes. A desconectar...")
          file.close()
          return
      else:
        
        print("\n-> Login feito com sucesso!")
        controlo_pass = 1
      
  if(controlo_user == 0):
    
    print("\n-> Utilizador inválido. A desconectar...")
    file.close()
    return
  if(controlo_pass):
    file.close()
    menulogin(user)

  

def registar():

  print("\n-> Insira o username e password com que se deseja registar.")

  cont = 0

  user = input("\nUsername:")

  
  f1 = open("base_de_dados.txt", 'a+')
  
  f1.seek(0)
  for line in f1:
    
    if (user == line.split()[0]):

      print("\n-> Utilizador já registado.")
      f1.close()
      return 

  
  password = input ("Password:")
  f1.write(user + " " + password + "\n")
  f1.close()
  print("\n-> Registo efetuado com sucesso!")

  

def main():

  resposta1 = ''

  print("-> Bem vindo ao sistema de login.")

  while(resposta1 != 'S'):

    resposta1 = input("\n\n \
    Login -------------------- prima 'L' e enter\n \
    Registar ----------------- prima 'R' e enter\n \
    Sair do programa --------- prima 'S' e enter\n\n").upper()

    if resposta1 == 'L':
      autenticar()

    elif resposta1 == 'R':
      registar()

    elif resposta1 == 'S':
      break

    else:
      print("\n-> Por favor insira apenas 'L', 'R' ou 'S' seguido de enter.")

 
main()
