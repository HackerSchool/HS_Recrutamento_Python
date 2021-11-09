# coding=utf-8
"""
O módulo Calculadora.
"""
import typing
import os

# Colocar as listas de operações por ordem de precedência na lista.
# Cada operação na mesma ordem de precedência das outras tem de estar numa sub-lista com as outras operações, sem
# nenhuma ordem específica.
# Exemplo abaixo.
OPERACOES_VALIDAS: typing.Final[list] = [["^"], ["*", "/", "%"], ["+", "-"]]

results_ants = [0]  # type: list[float]

def chamarCalculo() -> bool:
	"""
	| Realizar um cálculo.

	:return: True caso seja para continuar a calcular, False caso seja para parar
	"""
	global results_ants

	print("\n---")
	print("Cálculo || " + str(len(results_ants)) + " ||")

	expressao = input().replace(" ", "")
	#print(eval(expressao)) --> Não usar isto. Acho que às vezes dá resultados errados ("- 2 % 5 - 3 + 6 - 9 ** 4 * 7")
	# Retirar todos os espaços para não haverem problemas de alguém ter metido um espaço a menos ou algo assim.

	if expressao == "sair":
		return False

	# Para manter as ops todas com 1 char apenas (mais fácil), substituir as ops com 2 chars por 1 char
	expressao = "(" + expressao.replace("**", "^") + ")"
	for lista_ops in OPERACOES_VALIDAS:  # type: list[str]
		for op in lista_ops:  # type: str
			expressao = expressao.replace(op, " " + op + " ")

	#print(expressao)

	local_parents = [contador for contador, char in enumerate(expressao) if char == "(" or char == ")"]  # type: list[int]

	cont = 0
	while len(local_parents) > 0:
		local_parents = [contador for contador, char in enumerate(expressao) if char == "(" or char == ")"]

		#print(cont)
		#print(expressao[local_parents[cont+1]])
		#print(expressao[local_parents[cont]])
		if expressao[local_parents[cont+1]] != expressao[local_parents[cont]]:
			#print("Para calcular: " + expressao[local_parents[cont]+1:local_parents[cont+1]])
			resultado = calculo(expressao[local_parents[cont]+1:local_parents[cont+1]])  # type: float
			expressao = expressao[:local_parents[cont]] + str(resultado) + expressao[local_parents[cont+1]+1:]
			local_parents.pop(cont+1)
			local_parents.pop(cont)
			cont = -1
		cont += 1
		#print("local_parents - " + str(local_parents))
		#print("expressao - " + expressao)

	#print(local_parents)

	results_ants.append(float(expressao))

	print("-")
	print("Resultado: " + str(results_ants[-1]))

	return True

def calculo(expressao: str) -> float:
	expressao_lista = expressao.split()  # type: list[str]
	if expressao_lista[0] == "-":
		# Se a expressão começa por um menos, tem de se subtrair a alguma coisa. Então pôr um 0 no início. Simplifica...
		expressao_lista.insert(0, "0")

	for cont, i in enumerate(expressao_lista):
		i = i.lower()
		if i == "ans":
			expressao_lista[cont] = str(results_ants[-1])
		elif i.startswith("calc"):
			calc_num = int(i.split("calc")[1])  # type: int
			if calc_num < 0 or calc_num >= len(results_ants):
				print("Erro: cálculo nº " + str(calc_num) + " não encontrado.")

				return 0
			expressao_lista[cont] = str(results_ants[calc_num])

	for lista_ops in OPERACOES_VALIDAS:
		# (Porquê while? Porque não me entendo com o for...)
		cont = 0  # type: int
		while cont != len(expressao_lista):  # type: int
			op = expressao_lista[cont]  # type: str
			if op in lista_ops:
				num1 = float(expressao_lista[cont-1])  # type: float
				num2 = float(expressao_lista[cont+1])  # type: float

				# Não mudar a ordem de remoção abaixo... Ou se se trocar, pop(cont); pop(cont) --> não esquecer!
				expressao_lista.pop(cont + 1)
				expressao_lista.pop(cont)

				if op == "+":
					expressao_lista[cont - 1] = str(num1 + num2)
				elif op == "-":
					expressao_lista[cont - 1] = str(num1 - num2)
				elif op == "*":
					expressao_lista[cont - 1] = str(num1 * num2)
				elif op == "/":
					expressao_lista[cont - 1] = str(num1 / num2)
				elif op == "^":
					expressao_lista[cont - 1] = str(num1 ** num2)
				elif op == "%":
					expressao_lista[cont - 1] = str(num1 % num2)

				cont = -1
			cont += 1

	#print("expressao_lista - " + str(expressao_lista))

	return float(expressao_lista[0])

def main() -> None:
	"""
	Função de ativação da calculadora.
	"""
	global results_ants

	results_ants = [0]

	os.system("cls")
	print("----- Calculadora -----")
	print("---")

	while True:
		if not chamarCalculo():
			break
