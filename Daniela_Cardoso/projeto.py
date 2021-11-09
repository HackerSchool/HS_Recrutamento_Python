from app import menu as menu
from login import login as login
from login import register as register


def main():
    print("Bem vind@:\n")
    k=1
    f= open('registos.txt', '+w')
    while k==1:
        print('''\nO que desejas fazer?:
              a - Login
              b - Registar
              c - Quit
              ''')
        option = input("Opção(a,b ou c):\n")
        if option == 'a':
            k=login()
        elif option == 'b':
            register()
        elif option == 'c':
            print("Esperamos ver-te em breve")
            f.close()
            break
        else:
            print("Não foi reconhecido o comando")
    
    if k==0:
        menu()



main()