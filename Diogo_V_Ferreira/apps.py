import calculadora

def calculo():
    while True:
        print('''\n Bem vindo à calculadora!!
              
              Selecione a sua opção:
                  1- operações básicas (nivel 3)
                  2- expressão básica (nivel 5)
                  
                  3- Sair 
                  ''')
        opcao=input('Opção:\n')
        if opcao=='1':
            calculadora.opbasic()
        if opcao=='2':
            calculadora.expbasic()
        if opcao=='3':
            break