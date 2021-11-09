import registo
import loginFunc

def main():
    while True:
        print('''\n Bem vindo ao menu inicial!!
              
              Selecione a sua opção:
                  1- Login
                  2- Registar
                  3- Sair 
                  ''')
        opcao= input('Opção:\n')
        if opcao=='1':
            loginFunc.login()
        elif opcao=='2':
            registo.registo()
        elif opcao=='3':
            break
        else:
            print('ERRO: opção inválida, por favor tente novamente')

main()