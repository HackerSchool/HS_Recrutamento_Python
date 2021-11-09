import calculadora as c
import bot as b

def verifica(nomedeutilizador,palavrapasse): #verifica se este utilizador já está registado e se o login é válido
    ficheiro = open('login.txt','r')
    passe=palavrapasse + '\n'
    for linha in ficheiro:
        nomecheck=linha.split(' - ')[0]
        if nomecheck == nomedeutilizador: 
            passecheck=(linha.split(' - ')[1])
            if passecheck==passe:
                print("Login efetuado com sucesso\n")
                menulogin(nomedeutilizador,palavrapasse)
                return True
                break
            else:
                print("Palavra passe incorreta\n")
                return False
                break
    else:
        print("Nome de utilizador não registado\n")
        return False
    ficheiro.close()    

def registar(nome,passe):
    ficheiro = open('login.txt','a')
    ficheiro.write(nome + ' - ' +  passe + "\n")
    ficheiro.close()
    print("Utilizador registado com sucesso\n")
    return 0


def mudar(nomedeutilizador,palavrapasse,passenova):
    ficheiro = open('login.txt','r')
    linhas=ficheiro.readlines()
    ficheiro = open('login.txt','r')
    ficheiro.close()
    ficheiro = open('login.txt','w')
    for linha in linhas: #escrever todas as linhas menos a que queremos apagar
        if linha.strip('\n') != (nomedeutilizador + ' - ' + palavrapasse):
            ficheiro.write(linha)
    ficheiro.close()
    ficheiro = open('login.txt','a')
    ficheiro.write(nomedeutilizador + ' - ' +  passenova + "\n") #adiciona uma nova linha com o mesmo nome de
    #utilizador mas uma passe nova
    ficheiro.close()
    print("Palavra passe alterada com sucesso\n")
    return 0       
    
def menulogin(nomedeutilizador,palavrapasse):
    print("\nEscolhe uma ação:\n 1-Calculadora\n 2- ChatBot 3-Alterar palavra passe\n 4-Logout")
    opcao=input("Opção:\n")
    if opcao=='1':
        c.calcmain()
    if opcao=='2':
       b.botmain()
    if opcao=='3':
        passenova=input("Insira a palavra passe nova\n")
        mudar(nomedeutilizador,palavrapasse,passenova)
    if opcao=='4':
        main()
    return 0
    


def main():
    print("Escolhe uma ação:\n 1-Login\n 2-Registar\n 3-Sair do programa\n")
    acao=input("Ação:\n")
    if acao=='1':
        nomedeutilizador=input("Insira o nome de utilizador:\n")
        palavrapasse=input("Insira a palavra passe:\n")
        verifica(nomedeutilizador, palavrapasse) #dentro do verifica se verificar chama o menu login
    if acao=='2':
        nomedeutilizador=input("Insira o nome de utilizador a registar:\n")
        palavrapasse=input("Insira uma palavra passe:\n")
        registar(nomedeutilizador,palavrapasse)
    if acao=='3':
        print("A sair...")
    
main()
