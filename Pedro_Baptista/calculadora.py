# Função com dois modos, o primeiro pede 2 inteiros e uma operação e responde
# O segundo recebe uma string com uma operação e devolve o resultado, para isto
# procura a operação que está na string, parte a string ao meio e faz a operação

def calculadora():

    print('\nCalculadora inicializada!\n')

    while 1:
        print('Indique o modo de funcionamento pretendido:\n3: Receber dois números e uma operação')
        print('5: Receber string com uma operação\n')
        print('Inseriu:')

        mode = input()

        if mode == '3':
            n1 = input("\nInsira o primeiro número\n")
            n2 = input("\nInsira o segundo número\n")

            op = input("\nEscolha a operação: +, -, x, /, **, %\n")

            n1 = float(n1)
            n2 = float(n2)

            if op == '+':
                answer = n1 + n2
            elif op == '-':
                answer = n1 - n2
            elif op == 'x':
                answer = n1 * n2
            elif op == '/':
                answer = n1 / n2
            elif op == '**':
                answer = n1 ** n2
            elif op == '%':
                answer = n1 % n2
            

            print('\nA resposta é ', answer)

        
        if mode == '5':
            string = input("Insira a expressão a resolver (Operações: +, -, x, /, **, %)\n")

            if (string.find('+') != -1):
                n1 = float(string.split('+')[0])
                n2 = float(string.split('+')[1])
                answer = n1 + n2
                print('A resposta é \n', answer)
            elif (string.find('-') != -1):
                n1 = float(string.split('-')[0])
                n2 = float(string.split('-')[1])
                answer = n1 - n2
                print('A resposta é \n', answer)
            elif (string.find('x') != -1):
                n1 = float(string.split('x')[0])
                n2 = float(string.split('x')[1])
                answer = n1 * n2
                print('A resposta é \n', answer)
            elif (string.find('/') != -1):
                n1 = float(string.split('/')[0])
                n2 = float(string.split('/')[1])
                answer = n1 / n2
                print('A resposta é \n', answer)
            elif (string.find('**') != -1):
                n1 = float(string.split('**')[0])
                n2 = float(string.split('**')[1])
                answer = n1 ** n2
                print('A resposta é \n', answer)
            elif (string.find('%') != -1):
                n1 = float(string.split('%')[0])
                n2 = float(string.split('%')[1])
                answer = n1 % n2
                print('A resposta é \n', answer)

        y = input('Indique "1" se de seja sair, qualquer resposta caso contrário\n')
        if y == '1':
            return


