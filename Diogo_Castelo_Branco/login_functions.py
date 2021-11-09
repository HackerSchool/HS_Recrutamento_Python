import time

def menu(mode):
    b=1
    if(mode == 0):   #menu principal
        while(b==1):
            print("\nMenu de opções:\n\t1- Login\n\t2- Registar\n\t3- Sair do programa")
            opt = input("Escolha uma das 3 opções: ")

            if(opt == '1'):
                b=0
            elif(opt == '2'):
                b=0
            elif(opt == '3'):
                b=0
            else:
                print("\nSó são aceites os inteiros 1, 2 e 3. Volte a tentar de novo.\n") #se não der uma opção possível volta a repetir a pergunta
                time.sleep(2)
                b=1
        else:
            return opt
    else:             #menu de login
        while(b==1):
            print("\nAções possíveis:\n\t1- Calculadora\n\t2- Mudar Password\n\t3- Logout")
            opt = input("Escolha uma das 3 opções: ")

            if(opt == '1'):
                b=0
            elif(opt == '2'):
                b=0
            elif(opt == '3'):
                b=0
            else:
                print("\nSó são aceites os inteiros 1, 2 e 3. Volte a tentar de novo.\n") #se não der uma opção possível volta a repetir a pergunta
                time.sleep(2)
                b=1
        else:
            return opt

def ficheiro_novo(arg):    #verifica se o ficheiro já existe ou não (nome do ficheiro = arg)
    try:
        ficheiro = open(arg,'r')
        ficheiro = ficheiro.close()
        return False
    except:
        return True
        


def login():

    username = input("\nUsername: ")
    password = input("\nPassword: ")

    verify = ficheiro_novo("Users.txt")     

    if(verify == True):                                                                           #o ficheiro não existe
        print("Ainda não temos ninguém inscrito na plataforma. Podes ser tu o primeiro! \n")
        return '0'                                                                                #vai voltar ao menu principal
    else:
        ficheiro = open("Users.txt", "r")
        conteudo = ficheiro.read()                                       
        conteudo = conteudo.split()                                              #organiza os usernames e passwords num array desta forma [user1;pass1;user2;pass2]
        for i in range(len(conteudo)):           
            if(conteudo[i]==username):     #encontra o username no ficheiro
                if(conteudo[i+1]==password):          #a password corresponde à que está guardada no ficheiro
                    print("\nBem vindo ",conteudo[i])
                    ficheiro.close
                    time.sleep(2)
                    return conteudo[i]     #retorna o nome do user que fez login
                else:                                 #a password está errada
                    print("Password incorreta. A retornar ao menu principal...\n")
                    ficheiro.close
                    time.sleep(2)
                    return '0'

        print("Nome de utilizador incorreto. A retornar ao menu principal...\n")  #se ainda não tiver saído da função, significa que não encontrou correspondência ao user inserido, logo volta ao menu principal
        ficheiro.close
        time.sleep(2)
        return '0'



def registar():

    T = False
    while(T==False):                                #enquanto não forem garantidas as características do user e password ele repete o procedimento
        username = input("\nUsername: ")
        password = input("\nPassword: ")

        #para verificar se o user e pass têm ou não espaços
        username = username.split()
        password = password.split()     

        if(len(username)>1)or(len(password)>1):                        #caso tenha espaços volta a pedir o nome de user e pass
            print("Nem o teu username nem a password podem conter espaços, volta a tentar.\n\n")
            T=False
        else:
            str = username[0] + ' ' + password[0]                         #linha a inserir no ficheiro de texto

            verify = ficheiro_novo("Users.txt")

            if(verify == True):  
                ficheiro = open("Users.txt","w")                       #cria um ficheiro novo caso ainda não exista
                ficheiro.write(str)
                ficheiro.write('\n')
                ficheiro.close()
                T = True
            else:
                ficheiro = open("Users.txt","r")    #abre o que existir com a opção "r" para garantir que o username não se repete
                T = True
                for line in ficheiro:
                    if line.startswith(username[0]):
                        print("Esse nome já existe, volta a tentar.\n\n")
                        time.sleep(2)
                        T = False
                ficheiro.close()

                ficheiro = open("Users.txt","a")    #abre o ficheiro com a opção "a" para escrever o nome de user no fim
                ficheiro.write(str)
                ficheiro.write('\n')

                ficheiro.close()

    return


def mudar_pass(user):

    password = input("Nova Password:")
    ficheiro = open("Users.txt", "r")
    linhas = ficheiro.readlines()                               #organiza o conteudo do ficheiro por linhas e guarda em "linhas[]"
    ficheiro.close()                                            #Cada linha guarda o nome de utilizador e respetiva pass

    ficheiro = open("Users.txt", "w")                           #abre e apaga o conteudo do ficheiro
    for line in linhas:                                         #ciclo que faz a análise individual de cada linha
        u = line.split()                                        #separa o user da pass e guarda em u[]

        if u[0] != user:                                        #se o user não corresponder ao que está mudar de pass, então é colocado de volta no ficheiro
            ficheiro.write(line)
        else:                                                   #se o user for encontrado:
            str = ' '+ u[1]                                     #str = pass antiga
            password1 = ' ' + password                          #password1 = pass nova
            line = line.replace(str,password1)                  #na linha em questão muda-se trocam-se a pass antiga pela nova
            ficheiro.write(line)                                #coloca-se a linha já alterada no ficheiro
    ficheiro.close()
    
    return 
