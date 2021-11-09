def menu():
  while 1==1:
    print('Olá!')
    print("""
        Escolhe a tua opção:

        1- Registar
        2- Entrar
        3- Sair
        
        """)
    opcao=input()
    if opcao=='1':
      registar()

    elif opcao=='2' :
      entrar()
      break

    elif opcao=='3' :
      print('A Sair')
      break

    elif opcao!=['1','2','3']:
      print('Invalid input, try a valid one')

def registar():
  print('Como te chamas?')
  Utilizador=input()
  print('Define a tua password:')
  Password=input()
  while len(Password)<8:
    print('Password must be at least 8 characters long')
    Password=input()
    continue
  if len(Password)>=8:
    write(Utilizador,Password)
    print('Utilizador registado')
  
def write(Utilizador,Password):
  Adicionar=open('Dados de Utilizador.txt','a')
  Adicionar.write(Utilizador + '-' + Password +'\n')
  Adicionar.close

def entrar():
  Ler=open('Dados de Utilizador.txt','r')
  Ler=list(Ler)
  print('Nome de Utilizador?')
  Utilizador=input()
  print('Password?')
  Password=input()
  U_P=Utilizador+'-'+Password+'\n'
  if U_P in Ler:
    while 1==1:
      print('''
  Bemvindo!

          Opções:
          
          1-Alterar Password
          2-Calculadora
          3-Sair
          
          ''')
      opcao=input()
      if opcao=='1' :
        Alterar=open('Dados de Utilizador.txt','r+')
        linhas=Alterar.readlines()
        Alterar.seek(0)
        for i in linhas:
          if i != U_P:
            Alterar.write(i)
        Alterar.truncate()
        print('Define o teu novo utilizador e password:')
        Utilizador=input()
        Password=input()
        while len(Password)<8:
          print('Password must be at least 8 characters long')
          Password=input()
          continue
        if len(Password)>=8:
          write(Utilizador,Password)
          print('Utilizador registado')

      elif opcao=='2' :
        import Calculadora
        Calculadora.calculator()

      elif opcao=='3' :
        print('A Sair')
        break

      elif opcao!=['1','2','3']:
        print('Invalid input, try a valid one')

  else:
    print('Utilizador ou Password incorreto')
    menu()

menu()