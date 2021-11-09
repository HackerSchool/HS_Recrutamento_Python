from os import system

def main():
    while True:
        system("cls")
        print("\n    Calculadora Hacker\n")
        print("    Introduza '00' no seguinte campo para sair")
        equacao = input("\n    Introduza o que pretende resolver: ")

        if equacao == "00":
            break

        print(f"\n    Resultado: {eval(equacao)}")
        input("\n\n    Pressione Enter para reutilizar a calculadora")            

    