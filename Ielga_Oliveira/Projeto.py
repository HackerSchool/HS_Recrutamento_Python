import MenuAPP

def ler(id):
    ficheiro = open('Registo.txt','r')
    password = ""
    for linha in ficheiro:
        id2= linha.split('-')[0]
        if id==id2:
            password = linha.split('-')[1]
            break
    ficheiro.close()
    return password

def escrever(username,password):
    ficheiro = open('Registo.txt','a')
    ficheiro.write(username+ '-' + password + '\n')
    ficheiro.close()

def registar():
    username = input("username:\n")
    leitura = ler(username)
    if leitura != "":
        print("Este usuario ja se encontra registado")
    else:
        password = input("cont:\n")
        escrever(username,password)
        print("Registo efetuado com sucesso!")

def apagaLinha(id):
    ficheiro = open('Registo.txt')
    output = []
    for line in ficheiro:
        if not id in line:
            output.append(line)

    ficheiro.close()
    ficheiro2 = open('Registo.txt', 'w')
    ficheiro2.writelines(output)
    ficheiro2.close()

def mudarPassword():
    username = input("username:\n")
    apagaLinha(username)
    leitura = ler(username)
    if leitura != "":
        print("Este usuario ja se encontra registado")
    else:
        password = input("password:\n")
        escrever(username,password)
        print("Palavra-Passe alterada com Sucesso!")

def menuLogin():
    while True:
        print('''\nEscolhe a tua opcao
        1 - Calculadora
        2 - Mudar Password
        3 - Logout
        ''')
        opcao = input("opcao:\n")

        if opcao   == 1:
            MenuAPP.calculadora()
        elif opcao == 2:
            mudarPassword()
        elif opcao == 3:
            main()
        else:
            print("Introduza uma opcao que conste no Menu")
        
def login():
    username = input("username:\n")
    password_file = ler(username)
    password_input = input("password:\n")

    if password_file == "":
        print("Este usuario nao esta registado")
    
    elif password_file == password_input+'\n':
        print("Login efetuado")
        menuLogin()
    else:
        print("Credenciais incorretas")

def main():
    while True:
        print('''\nEscolhe a tua opcao
        1 - Login
        2 - Registar
        3 - Sair
        ''')
        opcao = input("opcao:\n")

        if opcao   == 1:
            print("Menu de Login")
            login()
        elif opcao == 2:
            registar()
        elif opcao == 3:
            exit()
        else:
            print("Introduza uma opcao que conste no Menu")
        
main()
