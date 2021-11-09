def welcome(nome):
  print("Olá", nome)
  return;

def read(identificador):
    ficheiro = open('registos.txt', 'r')
    conteudo = ""

    for linha in ficheiro:
        identificador2 = linha.split(' - ')[0]
        if identificador == identificador2:
            conteudo = linha.split(' - ')[1]
            ficheiro.close()
            return conteudo

    ficheiro.close()
    return conteudo

def write(identificador, conteudo):
    ficheiro = open('registos.txt', 'a')
    ficheiro.write(identificador + ' - ' + conteudo + '\n')
    ficheiro.close()

def register():
    identificador = input("Username:\n")
    leitura = read(identificador)
    if leitura != "":
        print("Esse username já está registado")
    else:
        conteudo = input("Password:\n")
        write(identificador, conteudo)
        nome = input("Como te chamas:\n")
        welcome(nome)

#MUDAR PASSWORD
def password(identificador):
    import os
    ficheiro = open('registos.txt', 'r')
    output = open('new_registos.txt', '+w')
    conteudo = input("Password:\n")

    for linha in ficheiro:
        identificador2 = linha.split(' - ')[0]
        if identificador == identificador2:
            output.write(identificador + ' - ' + conteudo + '\n')
        else:
            output.write(linha)
    os.replace('new_registos.txt', 'registos.txt')
    output.close()
    ficheiro.close()



def login():
    k=1
    identificador = input("username:\n")
    conteudo = read(identificador)
    pas = input("password:\n")
    
    
    if conteudo == "":
        print("username inválido")
        
    elif pas!=conteudo[:-1]:  
        print("password incorreta")
        print('''\nO que pretendes fazer?:
              1 - Mudar password
              2 - Novo registo
              3 - Voltar ao menu anterior
              ''')
        option = input("Opção(1,2 ou 3):\n")
        if option == '1':
            print("here")
            password(identificador)
        elif option == '2':
            register()
        elif option == '3':
            print("")
        else:
            print("Não foi reconhecido o comando")
    else:
        print("Sessão iniciada")
        k=0

    return k
