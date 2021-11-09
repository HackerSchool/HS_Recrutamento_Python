from os import system

def main():
    while True:
        system("cls")
        print("\n    Calculadora\n")
        print("    Introduza '00' em qualquer um dos campos para sair")
        n1 = int(input("\n    Número 1: "))

        if n1 == "00":
            break

        n2 = int(input("    Número 2: "))

        if n1 == "00":
            break

        operacao = input("    Operação (*,-,+,/): ")

        if operacao == "00":
            break


        if operacao == "+":
            print(f"\n    Resultado: {n1 + n2}")
        elif operacao == "-":
            print(f"\n    Resultado: {n1 - n2}")
        elif operacao == "*":
            print(f"\n    Resultado: {n1 * n2}")
        elif operacao == "/":
            print(f"\n    Resultado: {n1 + n2}")
        else:
            print("    Essa operação não é suportada")

        input("\n\n    Pressione Enter para reutilizar a calculadora")            

    