import calculadora

'''LER E ESCREVER'''

def ler(user):
    ficheiro = open('login.txt', 'r')
    pw = ""
  
    for linha in ficheiro.readlines(): #lê linhas, retirando o parágrafo da linha e colocando os dados numa lista
        aux = linha.strip('\n')
        credenciais = aux.split(' && ')
        if user == credenciais[0]: #Se username for igual a username das credenciais devolve password
            pw = credenciais[1]
            ficheiro.close()
            return pw
        
    ficheiro.close()
    return pw
      
        
def escrever(user, pw):
    ficheiro = open('login.txt', 'a')
    ficheiro.write(user + ' && ' + pw + '\n')
    ficheiro.close()


'''MENU DE LOGIN'''

def registar(): #regista o utilizador excepto quando o username é igual à password ou quando já existe
    print ("\nEscolha as suas credenciais:")
    username = input("Username: ")
    aux = ler(username)
    if aux != "": 
        print("\nUsername já utilizado\n")
    else:
        password = input("Password: ")
        if password != username:
            escrever(username, password)
        else:
            print("\nRegisto Inválido: Username e Password iguais")
           
def login():
    print ("\nColoque as suas credenciais:")
    username = input("Username: ")
    password = input("Password: ")
    aux = ler(username)
    if aux == "":
        print("\nUsername não existe\n")
    elif password != aux:
        print("\nPassword errada\n")
    elif password == aux:
        menu_login(username,password)
    
    
'''LOGIN'''

def menu_login(user,pw):
    while True:
        print('''\nLOGIN:\n
          Escolha as suas opções:
              1 - Escolher uma app
              2 - Mudar Password
              3 - Logout\n''')
        escolha = input("Opção: ")
        if escolha == '1':
            menu_apps()
        elif escolha == '2': #exclui casos em que nova password é igual à antiga ou igual ao username
            passnova = input("Password Nova: ")
            if passnova == user:
                print("\nMudança de Password Inválida: Username e Password iguais\n")
            elif passnova != pw:
                menu_pass(user,pw,passnova)
            elif passnova == pw:
                print("\nPassword já usada\n")
        elif escolha == '3': 
            print("\nLogout\n")
            break
        else:
            print("\nOpção não existe\n")


'''APPS'''

def menu_apps():
    while True:
        print('''\nAPPS:\n
          Escolha as suas opções:
              1 - Calculadora
              2 - Chat Bot
              3 - Tic-Tac-Toe\n''')
        escolha = input("Opção: ")
        if escolha == '1':
            calculadora.calculadora_1()
            break
        elif escolha == '2':
            print("\nNão existe\n")
        elif escolha == '3':
            print("\nNão existe\n")
        else:
            print("\nOpção não existe\n")
            
            
'''MUDAR PASSWORD'''
#abre ficheiro, lê-o muda a password e rescreve o ficheiro com a password alterada
def menu_pass(user, pw, pwnova):
    ficheiro = open('login.txt', 'r')
    cred = ficheiro.read()
    ficheiro.seek(0)
    for linha in ficheiro.readlines():
        aux = linha.strip('\n')
        cred_aux = aux.split(' && ')
        if cred_aux[0] == user: #evita substituir passwords iguais com usernames diferentes
            cred = cred.replace(pw, pwnova,1)
            break
        else:
            continue
    ficheiro.close()
    
    ficheiro = open('login.txt', 'w')
    ficheiro.write(cred)
    ficheiro.close()


'''main'''

def main():
    while True:
        print('''\nMENU DE LOGIN:\n
          Escolha as suas opções:
              1 - Login
              2 - Registar
              3 - Sair\n''')
        escolha = input("Opção: ")
        if escolha == '1':
            login()
        elif escolha == '2':
            registar()
        elif escolha == '3':
            print("\nA sair do programa\n")
            break
        else:
            print("\nOpção não existe\n")

main()
