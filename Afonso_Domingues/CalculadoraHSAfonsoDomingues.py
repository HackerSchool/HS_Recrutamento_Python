"""
Conjunto de funções que criam uma calculadora com vários modos e funcionalidades. Acesso à calculadora através do
programa do login. Utilização de ciclos try-except nas várias funções para permitir que o programa continue a correr
mesmo se o utilizador inserir um dado incorreto.

Autor: Afonso Domingues
Data: 07/11/2021
Contacto: afonso.silva.domingues@tecnico.ulisboa.pt
"""

# Importações para a representação de funções no gráfico
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Função principal da calculadora que realiza as chamadas às outras funções dependendo das entradas númericas
    fornecidas pelo utilizador. Criação de um menu com oito opções (input com duas operações, string com expressão de
    uma operação, string com uma expressão de múltiplas operações, solução de equações de uma variável, solução de
    equações de duas variáveis, resolução de sistemas matriciais (soma, multiplcação e traço de matrizes) e sair).
    """
    while True:
        try:
            print('-------------------Menu inicial calculadora--------------------')
            acao = int(input('\nEscolhe uma das seguintes ações marcando um dos números abaixo:\n\n\t1 - Input e duas '
                             'operações\n\t2 - String com expressão (uma operação)\n\t3 - String com expressão (várias '
                             'operações)\n\t4 - Equações de uma variável\n\t5 - Equações de duas variáveis\n\t6 - '
                             'Sistema matricial\n\t7 - Representação de funções\n\t8 - Sair\n\nNúmero: '))

            if acao == 1:
                calculadora_input()

            elif acao == 2:
                calculadora_str()

            elif acao == 3:
                calculadora_str_varios()

            elif acao == 4:
                res_eq_uma_var()

            elif acao == 5:
                res_eq_duas_var()

            elif acao == 6:
                sistema_matricial()

            elif acao == 7:
                rep_func()

            elif acao == 8:
                break

            else:
                raise ValueError

        except ValueError:
            print('\n')


def calculadora_input():
    """
    Função que define o cálculo de uma operação com 3 inputs sucessivos, os dois primeiros para os valores e o último
    para o operador.
    """

    def verificar_existencia_conta(x):
        """
        Função auxiliar com loop para prevenir que o utilizador insira uma conta num input de valor, evitando assim que
        a conta seja feita posteriormente com a chamada à função eval (utilizada para se poder usar ints e floats).
        """
        for i in x:
            for j in ('+', '-', 'x', '*', '**', '/', '%'):
                if i == j:
                    raise ValueError

    while True:
        try:
            num1 = input('Escreva o primeiro número ("exit" para sair): ')
            
            if num1 == 'exit':
                break
            
            num2 = input('Escreva o segundo número ("exit" para sair): ')
            
            if num2 == 'exit':
                break
            
            operador = input('Escreva o operador ("exit" para sair): ')
            
            if operador == 'exit':
                break
            
            verificar_existencia_conta(num1)
            verificar_existencia_conta(num2)

            num1, num2 = eval(num1), eval(num2)
            # Utilização da função eval para poder fazer cálculos com inteiros e floats em simultâneo. Se utilizássemos
            # a função float, também conseguiriamos o mesmo resultado mas as contas com inteiros teriam um resultado com
            # vírgula (ex: 1 + 2 em float é 1.0 + 2.0 = 3.0) e o programa seria mais lento.

            if operador == '+':
                print(str(num1) + ' + ' + str(num2) + ' =', num1 + num2, '\n')
            elif operador == '-':
                print(str(num1) + ' - ' + str(num2) + ' =', num1 - num2, '\n')
            elif operador == 'x' or operador == '*':
                print(str(num1) + ' x ' + str(num2) + ' =', num1 * num2, '\n')
            elif operador == '**':
                print(str(num1) + ' ** ' + str(num2) + ' =', num1 ** num2, '\n')
            elif operador == '/':
                print(str(num1) + ' / ' + str(num2) + ' =', num1 / num2, '\n')
            elif operador == '%':
                print(str(num1) + ' % ' + str(num2) + ' =', num1 % num2, '\n')
            else:
                raise ValueError

        except (NameError, ValueError):
            print('Valor incorreto, tenta novamente')


def calculadora_str():
    """
    Função que define o cálculo de uma expressão inserida diretamente sobre a forma de uma string. Se a expressão tiver
    mais do que um operador, só será calculado o valor da primeira conta.
    """
    while True:
        try:
            calculo = input('Escreva o cálculo a executar (separados por espaços), exit para terminar: ').split()

            if 'exit' in calculo:
                break

            if not isinstance(eval(calculo[0]), (int, float)) or not isinstance(eval(calculo[2]), (int, float)) or \
                    calculo[1] not in ('+', '-', 'x', '*', '**', '/', '%'):
                raise ValueError

            operador = calculo[1]

            if operador == '+':
                print(calculo[0] + ' + ' + calculo[2] + ' =', eval(calculo[0]) + eval(calculo[2]), '\n')
            elif operador == '-':
                print(calculo[0] + ' - ' + calculo[2] + ' =', eval(calculo[0]) - eval(calculo[2]), '\n')
            elif operador == 'x' or operador == '*':
                print(calculo[0] + ' x ' + calculo[2] + ' =', eval(calculo[0]) * eval(calculo[2]), '\n')
            elif operador == '**':
                print(calculo[0] + ' ** ' + calculo[2] + ' =', eval(calculo[0]) ** eval(calculo[2]), '\n')
            elif operador == '/':
                print(calculo[0] + ' / ' + calculo[2] + ' =', eval(calculo[0]) / eval(calculo[2]), '\n')
            elif operador == '%':
                print(calculo[0] + ' % ' + calculo[2] + ' =', eval(calculo[0]) % eval(calculo[2]), '\n')

        except(NameError, ValueError, IndexError, SyntaxError):
            print('Valor incorreto, tenta novamente')


def calculadora_str_varios():
    """
    Função que define o cálculo de uma expressão inserida diretamente sobre a forma de uma string com várias operações.
    """
    while True:
        try:
            calculo = input('Escreva o cálculo com múltiplas operações a executar (separadas por espaços), '
                            'exit para terminar: ')

            if calculo == 'exit':
                return
            
            calculo_copy = calculo  # Cópia para fazer o print na consola da conta inicialmente inserida
            calculo = calculo.split()

            ordem_prioridade_calculos = ('**', '/', 'x', '*', '-', '+')

            for operador in ordem_prioridade_calculos:
                i = 0

                while i < len(calculo):
                    if calculo[i] == operador:
                        if operador == '**':
                            calculo[i] = str(eval(calculo[i - 1]) ** eval(calculo[i + 1]))
                        elif operador == '/':
                            calculo[i] = str(eval(calculo[i - 1]) / eval(calculo[i + 1]))
                        elif operador == 'x' or operador == '*':
                            calculo[i] = str(eval(calculo[i - 1]) * eval(calculo[i + 1]))
                        elif operador == '-':
                            calculo[i] = str(eval(calculo[i - 1]) - eval(calculo[i + 1]))
                        elif operador == '+':
                            calculo[i] = str(eval(calculo[i - 1]) + eval(calculo[i + 1]))
                        # Substituição na lista do operador em questão pelo valor da conta
                        # ex: ['1','+','2'] --> ['1','3','2']

                        calculo.pop(i - 1)
                        calculo.pop(i)
                        # Remoção dos dois valores para os quais já fizemos a conta
                        # ex: ['1','3','2'] --> ['3']

                    i += 1

            print(calculo_copy, '=', eval(calculo[0]), '\n')

        except (NameError, ValueError, IndexError, SyntaxError):
            print('Valor incorreto, tenta novamente')


def res_eq_uma_var():
    """
    Função que define o cálculo da solução de uma equação com uma variável.
    """
    while True:
        try:
            a = input('Introduz o valor de "a", sendo "a" o coeficiente à frente da variável x na equação da forma ax +'
                      ' b = 0 (exit para terminar): ')

            if a == 'exit':
                break

            b = input('Introduz o valor de "b", sendo "b" o termo independente na equação da forma ax + b = 0: ')

            a, b = eval(a), eval(b)

            print('ax + b = 0, com a =', a, 'e b =', b, 'tem por solução x =', -b / a, '\n')

        except (ValueError, TypeError, NameError):
            print('\nValor incorreto, tenta novamente')


def res_eq_duas_var():
    """
    Função que define o cálculo da solução de uma equação de duas variáveis.
    """
    while True:
        try:
            a = input('Introduz o valor de "a", sendo "a" o coeficiente à frente da variável x na equação da forma ax +'
                      ' by + c = 0 (exit para terminar): ')

            if a == 'exit':
                break

            b = input('Introduz o valor de "b", sendo "b"  o coeficiente à frente da variável y na equação da forma ax '
                      '+ by + c = 0: ')
            c = input('Introduz o valor de "c", sendo "c"  o termo independente da equação da forma ax + by + c = 0: ')

            a, b, c = eval(a), eval(b), eval(c)

            print('ax + by + c = 0, com a =', a, ',', 'b =', b, 'e c =', c, 'tem por solução y =', (-a / b), 'x +',
                  (-c / b), '\n')

        except (NameError, ValueError, TypeError):
            print('\nValor incorreto, tenta novamente')


def sistema_matricial():
    """
    Função que engloba e define três operações diferentes sobre matrizes (soma, multiplicação e traço). Realização das
    operações de acordo com o valor numérico inserido pelo utilizador.
    """
    def soma_mat(matriz1, matriz2):
        """Função que define a soma de matrizes (Realizada na cadeira de Fundamentos da Programação)"""
        for i in range(len(matriz1)):  # Linhas das matrizes
            for j in range(len(matriz1[i])):  # Colunas das matrizes
                matriz1[i][j] = matriz1[i][j] + matriz2[i][j]
        print(matriz1)

    def multiplica_mat(matriz1, matriz2):
        """Função que define a multiplicação de matrizes (Realizada na cadeira de Fundamentos da Programação)"""
        matriz = []
        for i in range(len(matriz1)):  # Linhas da matriz 1
            linha = []
            for j in range(len(matriz2[0])):  # Colunas da matriz 2
                soma = 0
                for k in range(len(matriz2)):  # Linhas da matriz 2
                    soma += matriz1[i][k] * matriz2[k][j]
                linha += [soma]
            matriz += [linha]
        print(matriz)

    def traco_mat(matriz):
        """Função que define o cálculo do traço de uma matriz"""
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][i]
        print(soma)

    while True:
        try:
            operacao = input('Introduz a letra correspondente à operação a executar (S: soma, M: multiplicação, T: '
                             'Traço, exit para terminar): ')

            if operacao == 'exit':
                break

            elif operacao == 'S':
                m1 = eval(input('Introduz a matriz 1 sobre a forma de uma lista de listas (sendo cada sublista uma '
                                'linha da matriz): '))
                m2 = eval(input('Introduz a matriz 2 sobre a forma de uma lista de listas (sendo cada sublista uma '
                                'linha da matriz): '))

                if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
                    soma_mat(m1, m2)

                else:
                    raise ValueError

            elif operacao == 'M':
                m1 = eval(input('Introduz a matriz 1 sobre a forma de uma lista de listas (sendo cada sublista uma '
                                'linha da matriz): '))
                m2 = eval(input('Introduz a matriz 2 sobre a forma de uma lista de listas (sendo cada sublista uma '
                                'linha da matriz): '))

                if len(m1[0]) == len(m2):
                    multiplica_mat(m1, m2)

                else:
                    raise ValueError

            elif operacao == 'T':
                m = eval(input('Introduz a matriz sobre a forma de uma lista de listas (sendo cada sublista uma linha '
                               'da matriz): '))

                if len(m) == len(m[0]):
                    traco_mat(m)

                else:
                    raise ValueError

            else:
                raise ValueError

        except (ValueError, NameError):
            print('Matriz incorreta, tenta novamente')


def rep_func():
    """
    Função que define a representação gráfica de uma certa função inserida pelo utilizador num intervalo definido pelo
    mesmo.
    """
    dominio_min = eval(input('Introduz o valor mínimo "a" do domínio da função tal que x >= a: '))
    dominio_max = eval(input('Introduz o valor máximo "a" do domínio da função tal que x <= a: '))
    x = np.arange(dominio_min, dominio_max + 1, 1)  # Cria uma série de valores no domínio definido com step = 1
    func = input('Introduz a função f(x): ')

    plt.title('f(x) = ' + func)  # Adiciona um título ao gráfico
    plt.plot(x, eval(func), "b--", label="f(x)")  # Cria o gráfico
    plt.grid()  # Adiciona uma grelha ao gráfico
    plt.show()  # Mostra o gráfico
