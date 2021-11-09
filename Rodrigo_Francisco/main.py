import os, calc, ttt



def setcolor(a=0, b=0, c=0):
    if a == b == c == 0:
        print("\033[m", end="")
    else:
        font = "\033["
        if(a != 0):
            font += str(a)
        if(b != 0):
            if(font[-1] != "["):
                font += ";"
            font += str(b)
        if(c != 0):
            if(font[-1] != "["):
                font += ";"
            font += str(c)
        font += "m"
        print(font, end="")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login(log):
    clear()

    print("\nMenu de Login\n")
    access = ["", ""]

    while(True):
        access[0] = input("Nome de utilizador: ")
        access[1] = input("Password: ")

        if(access not in log):
            print("\nNome de utilizador ou password incorretas, deseja sair?")
            ans = input("[s/n] > ")
            if(ans == "s"):
                break
        else:
            logoptions(log, access)
            break

def registo(log):
    clear()
    access = ["",""]

    print("\nMenu de Registo\n")

    
    access[0] = str(input("Nome de utilizador: "))

    while(len(log) > 0 and access[0] in [user[0] for user in log]):
        print("\nNome de utilizador já existe!")
        access[0] = str(input("Nome de utilizador: "))
    
    access[1] = str(input("Password: "))
    teste = str(input("Password outra vez: "))
    
    while(access[1] != teste):
        print("\nPasswords não correspondem, tente outra vez!")
        access[1] = str(input("Password: "))
        teste = str(input("Password outra vez: "))

    log.append(access)
    clear()
    return log

def logoptions(log, user):
    clear()
    print("Login feito com sucesso!")

    print(f"\nBem-vindo, {user[0]}!")
    while(True):
        
        print("\nAs suas opções:\n[1] Apps\n[2] Definições de conta\n[3] Logout")
        option = input("> ").strip()
        if(option == "1"):
            clear()
            while(True):    
                print("\nApps:\n\n[1] Calculadora\n[2] Chat bot\n[3] Jogo do Galo\n[4] Voltar atrás")
                app = input("> ").strip()

                if(app == "1"):
                    clear()
                    calc.main(log, user)
                elif(app == "2"):
                    clear()
                    print("\nInfelizmente a aplicação \"Chat bot\" não está disponível de momento...")
                elif(app == "3"):
                    clear()
                    ttt.main(log, user)
                    
                else:
                    clear()
                    break
            
        elif(option == "2"):
            clear()
            while(True):    
                print("\nDefinições de conta:\n[1] Mudar nome de utilizador\n[2] Mudar password\n[3] Voltar atrás")
                setting = input("> ").strip()
                if(setting == "1"):
                    clear()
                    print("Mudar nome de utilizador:")
                    new_user = input("Novo nome: ")
                    while(len(log) > 1 and new_user in [user[0] for user in log]):
                        print("Nome de utilizador já existe!")
                        new_user = input("Novo nome: ")
                    for i in range(0, len(log)):
                        if(log[i] == user):
                            log[i][0] = new_user
                            user[0] = new_user
                    clear()

                elif(setting == "2"):
                    clear()
                    print("Mudar password:")

                    while(True):
                        old_pass = input("Password antiga: ")
                        if(old_pass == user[1]):
                            break
                        print("Password antiga está errada, deseja sair?")
                        ans = input("[s/n] > ")
                        if(ans == "s"):
                            break
                    if(old_pass != user[1]):
                        break

                    new_pass1 = input("Nova password: ")
                    new_pass2 = input("Nova password outra vez: ")

                    while(new_pass1 != new_pass2):
                        print("Passwords não correspondem, tente outra vez.")
                        new_pass1 = input("Nova password: ")
                        new_pass2 = input("Nova password outra vez: ")
                    
                    for i in range(0, len(log)):
                        if(log[i] == user):
                            log[i][1] = new_pass1
                            user[1] = new_pass1
                    clear()

                else:
                    clear()
                    break

        else:
            clear()
            print("\nSessão terminada")
            break

def readlog():
    log = []
    try:
        file = open("log", "r")
    except FileNotFoundError:
        return log

    for user in file:

        user = user.lstrip("[")
        user = user.rstrip("]\n")
        access = [i.strip().strip("'") for i in user.split(",")]
        log.append(access)

    file.close()
    return log

def updatelog(log):
    file = open("log", "w")

    for user in log:
        file.write(f"{user}\n")

    file.close

def main():
    clear()

    log = readlog()

    print("Bem vindo")

    while(True):
        
        print("\nEscolha uma das opções\n\n[1] Login\n[2] Registar\n[3] Sair do programa")

        option = input("> ").strip()

        if(option == "1"):
            login(log)
            
        elif(option == "2"):
            log = registo(log)
            
        else:
            clear()
            print("\nAté já!\n")
            break

    updatelog(log)

setcolor(7)
main()
setcolor()

