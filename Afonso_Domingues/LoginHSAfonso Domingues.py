"""
Conjunto de funções que criam um sistema de login que dá acesso à aplicação 'Calculadora', desenvolvida noutro ficheiro.
Utilização de ciclos try-except nas várias funções para permitir que o programa continue a correr mesmo se o utilizador
inserir um dado incorreto.

Autor: Afonso Domingues
Data: 07/11/2021
Contacto: afonso.silva.domingues@tecnico.ulisboa.pt
"""
import CalculadoraHSAfonsoDomingues


def main():
    """
    Função principal do programa, que realiza as chamadas às outras funções dependendo das entradas númericas fornecidas
    pelo utilizador. Criação de um menu com três opções (login, registar, sair).
    """
    while True:
        try:
            print('\n------------------------Página inicial-------------------------')
            acao = int(input('\nEscolhe uma das seguintes ações marcando um dos números abaixo:\n\n\t1 - Login\n\t'
                             '2 - Registar\n\t3 - Sair\n\nNúmero: '))
            if acao == 1:
                access_status = login()
                # login() devolve um tuplo com um bool seguido pelo nome do utilizador ou uma str vazia

                if access_status[0]:
                    menu_login(access_status[1])

                else:
                    print('----ACCESS DENIED (tentativas esgotadas), a fechar programa---')
                    break

            elif acao == 2:
                registar()

            elif acao == 3:
                resposta = protocolo_saida()  # protocolo_saida() devolve 'S' ou 'N' consoante a resposta do utilizador

                if resposta == 'S':
                    break

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print('\n')


def login():
    """
    Função que permite a autenticação de um utilizador presente na base de dados. Verificação da coerência dos dados
    inseridos com os dados presentes na base de dados. Contagem do número de tentativas para o nome de utiilizador e a
    palavra-passe e acesso barrado se o número de tentativas máximo for excedido.

    Return:
        Tuplo com dois arugmentos. O primeiro é um bool que tem o valor True se o utilizador inseriu os dados corretos
        sem passar o número de tentativas máximo, e que tem o valor False caso contrário. O segundo argumento é o nome
        do utilizador se o utilizador fizer o login com sucesso e é uma string vazia caso contrário.
    """
    tentativas_user = 5
    tentativas_password = 3

    while True:
        try:
            user_input = input('Introduz o teu nome de utilizador (cuidado com a utilização de maiúsculas e '
                               'minúsculas)\n\t--> ')

            with open('databaseHSAfonsoDomingues', 'r') as dbhs:
                for linha in dbhs:
                    user_check = linha.split(' - ')[0]

                    if user_check == user_input:
                        while True:
                            try:
                                password_input = input(f'Olá {user_input}, introduz a tua palavra-passe para teres '
                                                       f'acesso às apps\n\t--> ')
                                password_check = linha.split(' - ')[1]

                                if password_input + '\n' == password_check:
                                    return True, user_input

                                elif tentativas_password > 1:
                                    raise ValueError

                                else:
                                    return False, ''

                            except ValueError:
                                tentativas_password -= 1
                                print('Palavra-passe errada, nº de tentativas restantes:', tentativas_password)

                if tentativas_user > 1:
                    raise ValueError

                else:
                    return False, ''

        except ValueError:
            tentativas_user -= 1
            print('\nNome de utiizador inválido, tenta outra vez. Tentativas restantes:', tentativas_user)


def menu_login(user):
    """
    Função chamada caso os dados inseridos pelo utilizador estejam corretos. Criação de um menu com três opções (app da
    calculadora, mudar password e sair). Recurso à função main() do ficheiro da calculadora para inicializar a app.
    Mudança de palavra-passe verificando se a nova palavra-passe é igual à antiga, e registro da mudança na base de
    dados.

    Parametros:
        user (str): nome do utilizador que fez login (útil se for preciso redefinir a palavra-passe desse utilizador)
    """
    while True:
        try:
            opcao = int(input('\nEscolhe uma das seguintes ações marcando um dos números abaixo:\n\n\t1 - '
                              'Calculadora\n\t2 - Mudar password\n\t3 - Logout\n\nNúmero: '))

            if opcao == 1:
                CalculadoraHSAfonsoDomingues.main()

            elif opcao == 2:
                with open('databaseHSAfonsoDomingues', 'r') as dbhs:
                    linhas = dbhs.readlines()
                    status = ''  # Variável que muda de valor para 'done' se a palavra-passe já tiver sido mudada.

                    while True:
                        try:
                            if status == '':
                                palavra_passe_antiga = input('Introduz a tua palavra-passe antiga\n\t--> ')
                                i = 0

                                for linha in linhas:
                                    if linha == user + ' - ' + palavra_passe_antiga + '\n':
                                        palavra_passe_nova = input('Introduz a tua nova palavra-passe\n\t--> ')

                                        if palavra_passe_nova == palavra_passe_antiga:
                                            raise ValueError

                                        else:
                                            linhas.pop(i)
                                            linhas.append(user + ' - ' + palavra_passe_nova + '\n')
                                            # Remove a informação antiga do utilizador com índice i na lista de linhas
                                            # (readlines()) adiciona ao fim da lista a informação atualizada

                                            print('\nPalavra-passe mudada com sucesso')
                                            status = 'done'

                                            with open('databaseHSAfonsoDomingues', 'w') as dbhs:
                                                # Rewrite da base de dados com a informação atualizada
                                                for linha in linhas:
                                                    dbhs.write(linha)
                                                    print(linha)
                                            break  # Saida ciclo for da linha 135

                                    i += 1

                                raise ValueError

                            else:
                                break  # Saida ciclo while True

                        except ValueError:
                            print('\nPalavra-passe antiga errada ou palavra-passe nova igual à antiga. Tenta de novo.')

            elif opcao == 3:
                print('----------Fim de sessão, a voltar para o menu inicial----------')
                break

            else:
                raise ValueError

        except ValueError:
            print('\n')


def registar():
    """
    Função permitindo a criação de um novo utilizador na base de dados. Certificação que o nome de utilizador está
    disponível e criação da informação na base de dados.
    """
    while True:
        try:
            novo_utilizador = input('Introduz o teu nome de utilizador\n\t--> ')

            with open('databaseHSAfonsoDomingues', 'r') as dbhs:
                for linha in dbhs:
                    if novo_utilizador == linha.split(' - ')[0]:
                        raise ValueError

            with open('databaseHSAfonsoDomingues', 'a') as dbhs:
                nova_password = input('Introduz a tua palavra-passe\n\t--> ')
                dbhs.write(novo_utilizador + ' - ' + nova_password + '\n')

            print(f'Utilizador criado com sucesso, bem-vindo {novo_utilizador}!\n')

            break

        except ValueError:
            print('\nNome de utilizador em uso, escolhe outro')


def protocolo_saida():
    """
    Função permitindo finalizar a execução do programa e sair do ciclo while True da função main. Dupla verificação da
    intenção do utilizador.

    Return:
        'S' se o utilizador quiser sair, 'N' se não quiser sair.
    """
    while True:
        try:
            confirmacao = input('Tens a certeza que queres sair? (S para sair, N para cancelar)\n\t--> ')

            if confirmacao == 'S' or confirmacao == 's':
                confirmacao = input('Tens MESMO a certeza? (S para sair, N para cancelar)\n\t--> ')

                if confirmacao == 'S' or confirmacao == 's':
                    return 'S'

                elif confirmacao == 'N' or confirmacao == 'n':
                    return 'N'

                else:
                    raise ValueError

            elif confirmacao == 'N' or confirmacao == 'n':
                return 'N'

            else:
                raise ValueError

        except ValueError:
            print('Opção inválida, tenta outra vez.\n')


print('\n---------Bem-vind@ ao sistema de login da HackerSchool---------\n')
main()
print('------------------------Até à proxima!------------------------')
