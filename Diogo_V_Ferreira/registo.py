import auxiliares as aux

def registo():
    while True:
        UserName=input('Insira o nome de utilizador\n')
        pw=input('Insira a palavra passe\n')
        if UserName=="":
            print('Nome de utilizador inválido, por favor ecolha outro')
        elif aux.read(UserName)!="":
            print('Nome de utilizador já está em uso, por favor escoha outro')
        elif aux.write(UserName,pw)==0:
            print('Palavra passe inválida, por favor escolha outra')
        else:
            print('''Registo efectuado com sucesso!!
                  
                   |----------------------------------| 
                   |  A regressar ao menu inicial...  |
                   |----------------------------------|''')
            break
        