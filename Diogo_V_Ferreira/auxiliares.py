#escreve no registo a combinação do Username com a respetiva palavra passe
#devolve 1 se o registo teve sucesso, devolve 0 caso contrario
def write(UserName, PP):
    if  PP=="":
        return 0
    else:
        ficheiro=open('Registo.txt','a')
        ficheiro.write(UserName + ' - ' +PP+'\n')
        ficheiro.close
        return 1
 
 # recebe o identificador e devolve o conteudo presente nesse identificador
 #devolve "" se não existir o identificador
def read(Username):
    ficheiro=open('Registo.txt','r')
    conteudo=""
    for linha in ficheiro:
        IDcont = linha.split(' - ')
        if IDcont[0]==Username:
            conteudo= IDcont[1][0:-1]
            ficheiro.close()
            return conteudo
    ficheiro.close()
    return conteudo

def writein(UserName,newPP):
    ficheiro=open('Registo.txt','r')
    linhas=ficheiro.readlines()
    i=0
    while i<=len(linhas)-1:
        ID=linhas[i].split(' - ')[0]
        if ID==UserName:
            linhas[i]=UserName + ' - ' +newPP+'\n'
            i=len(linhas)
        i=i+1
    ficheiro.close()
    ficheiro=open('Registo.txt','w')
    ficheiro.writelines(linhas)
    ficheiro.close()
    