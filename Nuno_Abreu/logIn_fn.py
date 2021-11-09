# Funções de Login
import calc
import os


def chg(x, z):
    nome = z.name
    z.close()
    file = open(nome, 'r')
    crd2 = open('crd2.txt', 'a')
    for i in file:
        if i.find(x) == -1:
            crd2.write(i)
        else:
            while True:
                npass = input("New Password:")
                npass2 = input("New Password Check:")
                if npass != npass2:
                    print("New Password Check must be the same as New Password \n")
                else:
                    crd2.write(x + npass + '\n')
                    break
    file.close()
    file = open(nome, 'w')
    crd2.close()
    crd2 = open('crd2.txt', 'r')
    crd2r = crd2.read()
    file.write(crd2r)
    file.close()
    crd2.close()
    os.remove('crd2.txt')


def login():
    crd = open("credenciais.txt", 'r')
    crdr = crd.read()
    while True:
        uname = input("Username:")

        if len(uname) < 4:
            print("Username must have 4 characters or more")
        elif crdr.find(uname + '-') != -1:
            password = input("Password:")
            if crdr.find(uname + '-' + password) == -1:
                print("Credenciais incorretas")
            else:

                while True:
                    print(f'''Bem vind@ {uname}
                    
Pressione 1 para CALCULADORA
Pressione 2 para mudar a Password
Pressione 3 para sair''')
                    option = input("Opcao ")
                    if option == '1':
                        x = ''
                        while x != 's':
                            x = calc.main(uname)
                    elif option == '2':
                        chg(uname + '-', crd)
                    elif option == '3':
                        crd.close()
                        break
                    else:
                        print("Dumbass")
            break
        else:
            print("Username inesistente")
            crd.close()
            return


def ashley():
    pass


def registar():
    crd = open("credenciais.txt", 'r')
    uname = ''
    password = ''
    crdr = crd.read()
    while True:
        
        uname = input("Username: ")
        if len(uname) < 4:
            print("Username must have 4 characters or more")
        elif crdr.find(uname) >= 0:
            print("Username allready in use, please pick another. \n")

        else:
            break

    crd.close()

    while True:
        
        password = input("Password: ")
        password2 = input("Password Check: ")
        if password != password2:
            print("Passwords Check must be the same as Password \n")
        else:
            break
    crd = open('credenciais.txt', 'a')
    crd.write(uname + "-" + password + '\n')
    crd.close()
    print("Registo bem sucedido \n")


            
    
