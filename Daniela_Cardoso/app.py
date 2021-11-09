def menu():
    print("Bem vindo às funcionalidades da calculadora")
    aux=0
    while (aux==0):
        print('''\nEscolhe uma opção:
                x - Calculadora simples inteiros (numero 1, número 2, operação)
                y - Calculadora simples string 
                r - Calculadora múltiplas operações decimais
                h - Calculadora múltiplas operações inteiros
                z - Sair da app
                ''')
        option = input("Opção:\n")
        if option == 'x':
            sn1=input("número 1\n")
            op=input("operação\n")
            sn2=input("numero 2\n")
            n1=float(sn1)
            n2=float(sn2)
            num=calc_simples(n1, n2, op)
            print("O resultado é:" + str(num))
        elif option == 'y':
            exp=input("expressão (NúmeroOperaçãoNúmero sem espaços e vírgulas)\n")
            num=calc_2(exp)
            print("O resultado é:" + str(num))
        elif option == 'r':
            exp=input("Expressão(sem parentesis)\n")
            num=calc_3(exp)
            print("O resultado é:" + str(num))
        elif option == 'h':
            exp=input("Expressão(com ou sem parentesis)\n")
            num=new_calc(exp)
            print("O resultado é:" + str(num))
        elif option == 'z':
            print("Esperamos ver-te em breve")
            aux=1
        else:
            print("Não foi reconhecido o comando")
    return

def calc_simples(n1, n2, op):
    if op == '+':
        n3=n1+n2
    elif op == '-':
        n3=n1-n2
    elif op == 'x' or op== '*':
        n3=n1*n2
    elif op == '/' and n2 != 0:
        n3=n1/n2
    elif op == '%':
        n3=n1%n2
    elif op == '**':
        n3=pow(n1, n2)
    else:
        print("Não foi reconhecida a operação")
        n3=0
    return n3


def calc_2(calculo): #calculadora básica - 1 operação
    import re
    parts = re.split(r'(-?\d*\.?\d+)', calculo)
    n3=calc_simples(float(parts[1]), float(parts[3]), parts[2])

    return n3


def calc_3(calculo): #não faz potências nem cálculos com parentesis
    import re
    parts = re.split(r'(-?\d*\.?\d+)', calculo)

    #nao separa parentesis e operaçoes, separa negativos
    #newlist1 = [x for x in re.split('(-?\d+\.?\d*)', calculo) if x != '']

    #separa parentesis
    #newlist2=re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', calculo)

    #separa parentesis mas separa ** 
    #this=re.findall(r'-?\d+|[a-z]+|\W+?', calculo)

    del parts[0] #apagar espaço inicial
    #print(parts)


    i=0
    while True:
        x=parts[i]
        if x=='*' or x=='/' or x=='%':
            n3=calc_simples(float(parts[i-1]), float(parts[i+1]), parts[i])
            del parts[i-1]
            del parts[i-1]
            parts[i-1]=str(n3)
        elif x=='' and i==len(parts)-1:
            break
        else:
            i+=1

    i=0
    while True:
        x=parts[i]
        if x=='+' or x=='-' :
            n3=calc_simples(float(parts[i-1]), float(parts[i+1]), parts[i])
            del parts[i-1]
            del parts[i-1]
            parts[i-1]=str(n3)
        elif x=='' and i==len(parts)-1:
            break
        else:
            i+=1

    if len(parts)!=2:
        while len(parts)!=2:
            n3=float(parts[0])+float(parts[2])
            del parts[1]
            del parts[1]
            parts[0]=n3

    n3=float(parts[0])

    return n3


def new_calc(calculo):
    import re
    this=re.findall(r'-?\d+|[a-z]+|\W+?', calculo)
    #print(this)

    aux=0
    i=0
    p=0

    while aux==0:
        x=this[p]
        #OPERAÇÕES DENTRO DOS PARENTESIS
        if x=='(':
            i=p

            while True:
                x=this[i+1]
                if (x=='*' or x=='/') and (this[i+2]!='*'):
                    n3=calc_simples(float(this[i]), float(this[i+2]), this[i+1])
                    del this[i]
                    del this[i]
                    this[i]=str(n3)
                elif x=='*' and this[i+2]=='*':
                    op='**'
                    n3=calc_simples(float(this[i]), float(this[i+3]), op)
                    del this[i]
                    del this[i]
                    del this[i]
                    this[i]=str(n3)
                elif x==')':
                    break
                else:
                    i+=1
            i=p
            x=this[p]
        
            while True:
                x=this[i+1]
                if x=='+' or x=='-':
                    n3=calc_simples(float(this[i]), float(this[i+2]), this[i+1])
                    del this[i]
                    del this[i]
                    this[i]=str(n3)
                elif x==')':
                    break
                else:
                    i+=1

            if i-p!=1:
                n3=float(this[i])+float(this[p+1])
                del this[i]
                this[p+1]=n3
                del this[i]
                del this[p]

            else:
                del this[i+1]
                del this[p]

            if p==len(this)-1 or p==len(this):
                aux=1
        elif p==len(this)-1 or p==len(this):
            aux=1
        else:
            p+=1
        
    #OPERAÇÕES FORA DOS PARENTESIS POR ORDEM
    
    i=0
    while True:
        x=this[i]
        if (x=='*' or x=='/' or x=='%') and (this[i+1]!='*'):
            n3=calc_simples(float(this[i-1]), float(this[i+1]), this[i])
            del this[i-1]
            del this[i-1]
            this[i-1]=str(n3)
            if i==len(this)-1 or i==len(this):
                break
        elif x=='*' and this[i+1]=='*':
            op='**'
            n3=calc_simples(float(this[i-1]), float(this[i+2]), op)
            del this[i-1]
            del this[i-1]
            del this[i-1]
            this[i-1]=str(n3)
            if i==len(this)-1 or i==len(this):
                break
        elif i==len(this)-1 or i==len(this):
            break
        else:
            i+=1
    
    #print(this)

    i=0
    while True:
        x=this[i]
        if x=='+' or x=='-' :
            n3=calc_simples(float(this[i-1]), float(this[i+1]), this[i])
            del this[i-1]
            del this[i-1]
            this[i-1]=str(n3)
            if i==len(this)-1 or i==len(this):
                break
        elif i==len(this)-1 or i==len(this):
            break
        else:
            i+=1
    #ADICIONAR DOIS NÚMEROS QUE SOBREM CASO UM SEJA NEGATIVO E O SINAL ESTEJA LA INCORPORADO

    if len(this)!=1 and (x!='+' or x!='-'):
        while len(this)!=1:
            n3=float(this[0])+float(this[1])
            del this[1]
            this[0]=n3
        
    n3=float(this[0])

    print(n3)

    return n3