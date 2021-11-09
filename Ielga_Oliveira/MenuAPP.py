''' Neste Menu temos uma calculadora simples. Faz operacoes como adicao,subtracao,multiplicacao,divisao
potencia e percentagem. Tambem calcula todo o tipo de expressoes '''

def adicionar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2
  
def multiplicar(num1, num2):
    return num1 * num2
  
def dividir(num1, num2):
    return num1 / num2

def potencia(num1, num2):
    return pow(num1,num2)
    
def percentagem(num1,num2):
    percentage = 100 * float(num1)/float(num2)
    return str(percentage) + "%"

def calculadora():
    while True:
        print('''\nEscolhe a tua opcao
        1 - Adicionar
        2 - Multiplicr
        3 - Dividir
        4 - Subtrair
        5 - Potencia
        6 - Percentagem
        7 - Calcular uma expressao 
        8 - Sair
        ''')
        opcao = input("opcao:\n")

        if opcao == 1:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "+", num_2, "=",adicionar(num_1, num_2))
        elif opcao == 2:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "*", num_2, "=",multiplicar(num_1, num_2))
        elif opcao == 3:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "/", num_2, "=",dividir(num_1, num_2))
        elif opcao == 4:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "-", num_2, "=",subtrair(num_1, num_2))
        elif opcao == 5:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "**", num_2, "=",potencia(num_1, num_2))
        elif opcao == 6:
            num_1 = int(input("Introduza o primeiro numero: "))
            num_2 = int(input("Introduza o segundo numero: "))
            print(num_1, "%", num_2, "=",percentagem(num_1, num_2))  
        elif opcao == 7:
            expr = input("Introduza a expressao:\n")
            print("resultado: " + str(eval(expr)))
        elif opcao == 8:
            exit()
        else:
            print("Introduza uma opcao que conste no Menu")



  


  

    
  

 
  

    
  

