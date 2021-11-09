# coding=utf-8
"""
O módulo Jogo do Galo.
"""
import os
import typing
import random

CHARS_DISPONIVEIS: typing.Final[tuple[str, str]] = ("X", "O")

ESCOLHA_HUMANO: typing.Final[str] = "H"
ESCOLHA_PC_BURRO: typing.Final[str] = "B"
ESCOLHA_PC_INTELIGENTE: typing.Final[str] = "I"

matriz_simbolos = []


def imprimirTabuleiro() -> None:
	"""
	| Imprimir o tabuleiro de jogo com os Xs and Os nos locais selecionados no *array_simbolos*.
	"""

	print(f"C   1   2   3  ")
	print(f"L _____________")
	print(f"1 | {matriz_simbolos[0][0]} | {matriz_simbolos[0][1]} | {matriz_simbolos[0][2]} |")
	print(f"2 | {matriz_simbolos[1][0]} | {matriz_simbolos[1][1]} | {matriz_simbolos[1][2]} |")
	print(f"3 | {matriz_simbolos[2][0]} | {matriz_simbolos[2][1]} | {matriz_simbolos[2][2]} |")
	print(f"  ¯¯¯¯¯¯¯¯¯¯¯¯¯")


def jogar(jogador: int, escolha: str) -> bool:
	"""
	| Colocar o jogador selecionado a fazer uma jogada.

	:param escolha: uma das constantes globais
	:param jogador: o número do jogador (ou 0 ou 1)

	:return: True se for para continuar a jogar, False caso contrário
	"""

	if jogador == 0 or escolha == ESCOLHA_HUMANO:
		print("Jogador " + str(jogador+1))

		coluna = int(input("Coluna: "))-1  # type: int
		linha = int(input("Linha: "))-1  # type: int
		matriz_simbolos[linha][coluna] = CHARS_DISPONIVEIS[jogador]
	elif escolha == ESCOLHA_PC_BURRO:
		parar = False  # type: bool
		while not parar:
			coluna = random.randrange(0, 3)  # type: int
			linha = random.randrange(0, 3)  # type: int
			if matriz_simbolos[linha][coluna] == " ":
				matriz_simbolos[linha][coluna] = CHARS_DISPONIVEIS[jogador]
				parar = True

	imprimirTabuleiro()
	if verificarGanhos():
		# Se alguém ganhou, para o jogo
		return False
	# Caso contrário, verificar se o tabuleiro encheu.
	contagem_simbolos = 0  # type: int
	for linha in matriz_simbolos:  # type: list[str]
		for simbolo in linha:  # type: str
			if simbolo != " ":
				contagem_simbolos += 1
	if contagem_simbolos == 9:
		# Se encheu, parar o jogo
		return False

	# Se nada disto aconteceu, continuar o jogo
	return True


def verificarGanhos() -> bool:
	"""
	| Verifica se algum jogador ganhou.

	:return: True caso alguém tenha ganho, False caso contrário
	"""

	for linha in range(0, 3):
		prim_simbolo = matriz_simbolos[linha][0]
		if prim_simbolo == " ":
			continue

		simbolos_iguais = True
		for coluna in range(1, 3):
			if matriz_simbolos[linha][coluna] != prim_simbolo:
				simbolos_iguais = False
				break

		if simbolos_iguais:
			print("O jogador " + str(CHARS_DISPONIVEIS.index(prim_simbolo)+1) + " ganhou.")
			input("Clica no ENTER para sair do jogo...")
			return True

	for coluna in range(0, 3):
		prim_simbolo = matriz_simbolos[0][coluna]
		if prim_simbolo == " ":
			continue

		simbolos_iguais = True
		for linha in range(1, 3):
			if matriz_simbolos[linha][coluna] != prim_simbolo:
				simbolos_iguais = False
				break

		if simbolos_iguais:
			print("O jogador " + str(CHARS_DISPONIVEIS.index(prim_simbolo)+1) + " ganhou.")
			input("Clica no ENTER para sair do jogo...")
			return True

	prim_simbolo = matriz_simbolos[0][0]
	if prim_simbolo != " ":
		simbolos_iguais = True
		for i in range(0, 3):
			if matriz_simbolos[i][i] != prim_simbolo:
				simbolos_iguais = False

		if simbolos_iguais:
			print("O jogador " + str(CHARS_DISPONIVEIS.index(prim_simbolo)+1) + " ganhou.")
			input("Clica no ENTER para sair do jogo...")
			return True

	prim_simbolo = matriz_simbolos[0][2]
	if prim_simbolo != " ":
		simbolos_iguais = True
		for i in range(0, 3):
			if matriz_simbolos[i][2-i] != prim_simbolo:
				simbolos_iguais = False

		if simbolos_iguais:
			print("O jogador " + str(CHARS_DISPONIVEIS.index(prim_simbolo)+1) + " ganhou.")
			input("Clica no ENTER para sair do jogo...")
			return True

	return False


def main() -> None:
	"""
	| Função de ativação do jogo.
	"""
	global matriz_simbolos

	os.system("cls")
	print("----- Jogo do Galo -----")
	print("---")

	print(f"""\nCarregar em:
	- {ESCOLHA_HUMANO} para jogar contra um jogador humano
	- {ESCOLHA_PC_BURRO} para jogar contra o PC em modo burro
	- S para sair""")
	#- {ESCOLHA_PC_INTELIGENTE} para jogar contra o PC em modo inteligente

	escolha = ""  # type: str
	while escolha not in (ESCOLHA_HUMANO, ESCOLHA_PC_BURRO, ESCOLHA_PC_INTELIGENTE, "S"):
		escolha = input("Opção: ").upper()

	if escolha == "S":
		return

	matriz_simbolos = [
		[" ", " ", " "],
		[" ", " ", " "],
		[" ", " ", " "],
	]

	imprimirTabuleiro()

	while True:
		if not jogar(0, escolha):
			break
		if not jogar(1, escolha):
			break
