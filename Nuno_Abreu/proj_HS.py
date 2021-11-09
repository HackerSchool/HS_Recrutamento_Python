

import logIn_fn as lgn
 

def main():
    while True:
        print('''Bem Vindo ao Super Fantastico Programa da HS do Abreu 

Pressiona 1 para logIn 
Pressiona 2 para Registar 
Pressiona 3 para Sair 
        ''')
        option = input("Opcao ")
        if option == '1':
            lgn.login()
        elif option == '2':
            lgn.registar()
        elif option == '3':
            print("*closing WinXP sounds*")
            break
        else:
            print("Dumbass")


if __name__ == "__main__":
    main()
