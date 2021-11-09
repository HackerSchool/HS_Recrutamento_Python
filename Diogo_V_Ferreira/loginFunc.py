import auxiliares as aux
import apps

def login():
    i=1
    while True:
        if i>3:
            print('''Número máximo de tentativas alcançado!
                  
                   |----------------------------------| 
                   |  A regressar ao menu inicial...  |
                   |----------------------------------|''')
            break
        else:
            print('\n Tentativa '+str(i)+'/3')
            UserName= input('Insira o seu nome de utilizador\n')
            pw=input('Insira a sua palavra passe\n')
            if UserName=="" or pw=="":
                print('Autenticação falhada, por favor tente de novo')
                i=i+1
            elif aux.read(UserName)==pw:
                print('Autenticação aprovada!')
                postlogin(UserName,pw)
                break
            else:
                print('Autenticação falhada, por favor tente de novo')
                i=i+1

def postlogin(UN,pw):
    while True:
         print('''\n              
              Selecione a sua opção:
                  1- App: Calculadora
                  2- Mudar palavra passe
                  3- Logout 
                  ''')
         opcao=input('opção:\n')   
         if opcao=='1':
            apps.calculo()
         elif opcao=='2':
            changepw(UN,pw)
         elif opcao=='3':
            print('''                  
                   |----------------------------------| 
                   |  A dar Logout e regressar ao     |
                   |          menu inicial...         |
                   |----------------------------------|''')
            break
         else:
            print('ERRO: opção inválida, por favor tente novamente')

def changepw(UN,pw):
    while True:
        Newpw=input('Insira a nova palavra passe\n')
        if Newpw=="":
            print('Palavra passe inválida, por favor escolha outra')
        else:
            aux.writein(UN,Newpw)
            print('Palavra passe alterada com sucesso!')
            break
        
            
    