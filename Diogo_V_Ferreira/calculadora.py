def opbasic():
    while True:
        n1=input('Inserir o primeiro valor da operação:\n')
        n2=input('Inserir o segundo valor da operação:\n')
        print('''operadores disponiveis:
                + -> soma
                - -> subtração
                * -> multiplicação
                / -> divisão
                % -> resto da divisão inteira
                ^ -> exponenciação\n''')
        op=input('Inserir o operador pretendido\n')
        if not( op!="" and (op in '+-*/%^') and n1.isnumeric() and n2.isnumeric() ):
            print('ERRO: argumentos invalidos')
        elif op=='+':
            print('O resultado é: '+ str(float(n1)+float(n2)))
        elif op=='-':
            print('O resultado é: '+ str(float(n1)-float(n2)))
        elif op=='*':
            print('O resultado é: '+ str(float(n1)*float(n2)))
        elif op=='/':
            print('O resultado é: '+ str(float(n1)/float(n2)))
        elif op=='%':
            print('O resultado é: '+ str(float(n1)%float(n2)))     
        elif op=='^':
            print('O resultado é: '+ str(float(n1)**float(n2)))  
        print('''\n 1-voltar          2-continuar''')
        opcao=input('voltar ou continuar??\n')
        if opcao=='1':
            break

def expbasic():
    while True :
        print('''\n Este programa recebe uma expressão com apenas uma operação e devolve o resultado.
 Escrever a expressão sem espaços e selecionar a operação de acordo com a lista:
                + <- soma
                -- <- subtração
                * <- multiplicação
                / <- divisão
                % <- resto da divisão inteira
                ^ <- exponenciação\n''')
        exp=input('Inserir a expressão:\n')
        if " " in exp:
            print('ERRO: espaços presentes na expresssão, tente de novo')
        elif '*' in exp:
            ns=exp.split('*')
            print('O resultado é: '+ str(float(ns[0])*float(ns[1])))
        elif '/' in exp:
            ns=exp.split('/')
            print('O resultado é: '+ str(float(ns[0])/float(ns[1])))
        elif '%' in exp:
            ns=exp.split('%')
            print('O resultado é: '+ str(float(ns[0])%float(ns[1])))
        elif '^' in exp:
            ns=exp.split('^')
            print('O resultado é: '+ str(float(ns[0])**float(ns[1])))
        elif '+' in exp:
            ns=exp.split('+')
            print('O resultado é: '+ str(float(ns[0])+float(ns[1])))
        elif '--' in exp:
            ns=exp.split('--')
            print('O resultado é: '+ str(float(ns[0])-float(ns[1])))   
            
            
        print('''\n 1-voltar          2-continuar''')
        opcao=input('voltar ou continuar??\n')
        if opcao=='1':
            break
            