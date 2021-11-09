from os import system
from time import sleep
from random import randint

from modules.calculator import main as calc
from modules.calculatorhacker import main as calchacker
from modules.tictactoeai import main as tictactoeai
from modules.tictactoe import main as tictactoe
from modules.snakeplot import game as snakeplot

def registrar(username, password):
    entries = get_entries()

    for entry in entries:
        entry = entry[1:]

        user, pw = entry.split(":")
        if user == username:
            return False

    #register
    entries.append(f"{randint(1,9)}{username}:{password}")

    #update entries
    update_entries(entries)

    return True

def login(username, password):

    entries = get_entries()

    for entry in entries:
        entry = entry[1:]

        user, pw = entry.split(":")

        if user == username and pw == password:
            return True

    return False

def logado(username):
    while True:
        system("cls")

        choice = input(f'''
    LOGADO COMO {username.upper()}

    1 - Calculadora
    2 - Calculadora (Hacker)
    ------------------------
    3 - TicTacToe
    4 - TicTacToe (AI)
    ------------------------
    5 - Snake (RUNNN!!!!!!)
    ------------------------

    0 - Sair
    00 - Alterar Password

    >>> ''')

        #clean once again
        system("cls")
        if choice == "1":
            calc()
        elif choice == "2":
            calchacker()
        elif choice == "3":
            tictactoe()
        elif choice == "4":
            tictactoeai()
        elif choice == "5":
            snakeplot()
        elif choice == "0":
            break
        elif choice == "00":
            print("\n    PASSWORD MANAGER\n")
            print("\n    Deixe os campos vazios para voltar ao menu\n")

            password = input("    Password atual: ")
            new_password = input("    Password Nova: ")

            confirm_new_password = input("    Reintroduza a Password Nova: ")

            if password == new_password == confirm_new_password == "":
                print("\n    Voltando para o menu de login..")
                sleep(2)

            elif confirm_new_password == new_password:
                returned = change_password(username, password, new_password)

                if returned:
                    print("\n    Password alterada com sucesso..")
                    print("    Voltando para o menu de login..")
                    sleep(2)
                else:
                    print("    A password que introduziu está errada..")
                    print("    Voltando para o menu de login..")
                    sleep(2)


            else:
                print("\n    As passwords que introduziu não coincidem")
                print("    Voltando para o menu de login..")
                sleep(1.5)

def change_password(username, password, new_password):
    entries = get_entries()

    for index, entry in enumerate(entries):

        entry = entry[1:]

        user, pw = entry.split(":")
        if user == username and pw == password:
            entries[index] = f"{randint(1,9)}{username}:{new_password}"

            #update
            update_entries(entries)

            return True

    return False

def c_encode(string):
    #normalize
    string = string.replace("\n", "").strip()

    unique_value = int(string[0])

    password_username = string[1:]

    #general cifra
    general_code = unique_value

    encoded = []

    for string in password_username.split(":"):
        #decode string
        encoded_string = []

        for index, caracter in enumerate(string):
            if not caracter.isalpha():
                if caracter.isnumeric():
                    caracter = f"{caracter}{randint(1,9)}"
                    skip = True
                encoded_string.append(caracter)
                continue

            ascii_code = ord(caracter) - ord("a")

            #add general code
            ascii_code += general_code

            #add individual
            if index % 5 == 0:
                ascii_code += 63
            elif index % 2 == 0:
                ascii_code -= 23
            else:
                ascii_code += 4

            #cycle trough
            cycled_ascii = ascii_code % 26

            new_caracter = chr(cycled_ascii + ord("a"))

            encoded_string.append(new_caracter)

        #join string
        encrypted_string = "".join(encoded_string)

        #add to the encoded list
        encoded.append(encrypted_string)

    return f"{unique_value}{':'.join(encoded)}"

def c_decode(string):
    #normalize
    string = string.replace("\n", "").strip()

    unique_value = int(string[0])

    password_username = string[1:]

    #general cifra
    general_code = unique_value

    encoded = []

    for string in password_username.split(":"):
        #decode string
        encoded_string = []

        skip = False
        for index, caracter in enumerate(string):
            if skip:
                skip = False
                continue

            if not caracter.isalpha():
                if caracter.isnumeric():
                    skip = True

                encoded_string.append(caracter)
                continue

            ascii_code = ord(caracter) - ord("a")

            #subtract general code
            ascii_code -= general_code

            #subtract individual
            if index % 5 == 0:
                ascii_code -= 63
            elif index % 2 == 0:
                ascii_code += 23
            else:
                ascii_code -= 4

            #cycle trough
            cycled_ascii = ascii_code % 26

            new_caracter = chr(cycled_ascii + ord("a"))

            encoded_string.append(new_caracter)

        #join string
        encrypted_string = "".join(encoded_string)

        #add to the encoded list
        encoded.append(encrypted_string)

    return f"{unique_value}{':'.join(encoded)}"

def get_entries():
    #get them from the "cats"
    with open("database.jpg", "r", encoding="ISO-8859-1") as f:
        lines = f.readlines()

    decoded_entries = []

    found = False

    for line in lines:
        #normalize line
        line = line.replace("\n", "").strip()

        #check interval
        if line == "======================":
            #invert the bool
            found = not found
            continue

        if found and line != "":
            #decode
            decoded_entries.append(c_decode(line))

    return decoded_entries

def update_entries(entries):
    entries.insert(0, "\n======================")
    entries.append("======================")

    with open("database.jpg", "rb") as f:
        content = f.readlines()[:4053]

    for entry in entries:
        if "======================" in entry:
            content.append(f"{entry}\n".encode())
        else:
            content.append(f"{c_encode(entry)}\n".encode())

    #write binary
    with open("database.jpg", "wb") as f:
        f.writelines(content)




def main():
    while True:
    #clean screen
        system("cls")
        choice = input('''
    BEM-VINDO

    1 - Login
    2 - Registrar

    0 - sair

 >>> ''')

        #clean once again
        system("cls")

        if choice == "1":
            print("\n    LOGIN\n")
            username = input("    Username: ").strip()
            password = input("    Password: ").strip()


            #registrar
            returned = login(username, password)

            if returned:
                print("    Logado com sucesso")
                print("    Redirecionando..")
                sleep(1)
                logado(username)
            else:
                print("    Username/Password errados")
                print("    Voltando para o menu inicial em 3 segundos..")
                sleep(3)

        elif choice == "2":
            print("\n    REGISTRAR\n")
            username = input("    Username: ").strip()
            password = input("    Password: ").strip()


            #registrar
            returned = registrar(username, password)

            if returned:
                print("    Registado com sucesso, pode agora usar as suas credenciais para dar login\n")
            else:
                print("    O username que escolheu já se encontra registado\n")
                print("    Voltando para o menu em 3 segundos..")
                sleep(3)

        elif choice == "0":
            print("Saindo..")
            exit()
        else:
            print("Escolha errada")




if __name__ == "__main__":
    main()
