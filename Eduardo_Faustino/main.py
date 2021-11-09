# coding=utf-8
"""
Módulo principal.
"""
import os
import typing
import time
import getpass

# Importação de módulos
import calculadora
import jogoGalo
import chatBot

utilizador_ligado = ""  # type: str

SEPARADOR_FICHEIRO_1: typing.Final[str] = " \\\\\\/// "
SEPARADOR_FICHEIRO_2: typing.Final[str] = " ///\\\\\\"


def menuPrincipal() -> None:
	"""
	| Menu Principal.
	"""
	global utilizador_ligado

	ESCOLHA_REGISTAR: typing.Final[str] = "R"
	ESCOLHA_LOGIN: typing.Final[str] = "I"
	ESCOLHA_SAIR: typing.Final[str] = "S"

	os.system("cls")
	print("----- Menu Principal -----")
	print("---\n")
	print(f"""Carrega em:
	- {ESCOLHA_LOGIN} para Iniciar Sessão
	- {ESCOLHA_REGISTAR} para Registar
	- {ESCOLHA_SAIR} para Sair do Programa""")
	n_estupidezes = 0
	escolha = ""  # type: str
	while escolha not in (ESCOLHA_REGISTAR, ESCOLHA_LOGIN, ESCOLHA_SAIR):
		escolha = input("Opção: ").upper()
		n_estupidezes += 1
	if n_estupidezes >= 10:
		print("Conseguiste o prémio de acertar ao calhas!!!")

	if escolha in (ESCOLHA_REGISTAR, ESCOLHA_LOGIN):
		if escolha == ESCOLHA_LOGIN:
			menuLogin()
		else:
			menuRegistar()
	else:
		print("A sair em 3 segundos...")
		time.sleep(3)
		exit(0)


def menuRegistar() -> None:
	"""
	| Menu de Registo.
	"""
	os.system("cls")
	print("----- Menu de Registo -----")
	print("---\n")
	print("Por favor insere os teus dados para te registarmos na aplicação.")
	nome, passe = input("Utilizador: "), getpass.getpass("Passe: ")  # type: str

	with open("utilizadores.txt", "r") as ficheiro:
		linhas = ficheiro.readlines()  # type: list[str]
		if (nome + SEPARADOR_FICHEIRO_1) in "\n".join(linhas):
			print("Aviso: Utilizador já existente.")
		else:
			linhas.append(nome + SEPARADOR_FICHEIRO_1 + passe + SEPARADOR_FICHEIRO_2)
			with open("utilizadores.txt", "w") as ficheiro_2:
				ficheiro_2.writelines(linhas)
			print("Utilizador registado com sucesso.")

	print("A voltar para o menu principal em 3 segundos...")
	time.sleep(3)
	menuPrincipal()


def menuLogin() -> None:
	"""
	| Menu de Início de Sessão.
	"""
	global utilizador_ligado

	ESCOLHA_CALC: typing.Final[str] = "C"
	ESCOLHA_JOGO_GALO: typing.Final[str] = "G"
	ESCOLHA_CHAT_BOT: typing.Final[str] = "B"
	ESCOLHA_MUDAR_PASSE: typing.Final[str] = "M"
	ESCOLHA_TERM_SESSAO: typing.Final[str] = "T"

	os.system("cls")
	print("----- Menu de Início de Sessão -----")
	print("---\n")

	if utilizador_ligado == "":  # Ao voltar a este menu, não voltar a pedir credenciais se o utilizador já inicou sessão
		print("Por favor insere os teus dados para te iniciarmos a sessão na aplicação.")
		nome, passe = input("Utilizador: "), getpass.getpass("Passe: ")  # type: str

		with open("utilizadores.txt", "r") as ficheiro:
			texto = ficheiro.read()  # type: str
			if (nome + SEPARADOR_FICHEIRO_1 + passe + SEPARADOR_FICHEIRO_2) in texto:
				utilizador_ligado = nome
				print("Sessão iniciada com sucesso. A entrar em 3 segundos...")
				time.sleep(3)
			else:
				print("Dados incorretos ou utilizador não encontrado. A voltar em 3 segundos...")
				time.sleep(3)
				menuPrincipal()

	print(f"""\nCarrega em:
	- {ESCOLHA_CALC} para entrar na Calculadora
	- {ESCOLHA_JOGO_GALO} para entrar no Jogo do Galo
	- {ESCOLHA_CHAT_BOT} para entrar no Chat Bot
	- {ESCOLHA_MUDAR_PASSE} para Mudar de palavra-passe
	- {ESCOLHA_TERM_SESSAO} para Terminar sessão""")

	escolha = ""  # type: str
	while escolha not in (ESCOLHA_CALC, ESCOLHA_JOGO_GALO, ESCOLHA_CHAT_BOT, ESCOLHA_MUDAR_PASSE, ESCOLHA_TERM_SESSAO):
		escolha = input("Opção: ").upper()

	if escolha == ESCOLHA_MUDAR_PASSE:
		nova_passe = getpass.getpass("\nPor favor introduz a nova palavra-passe: ")
		with open("utilizadores.txt", "r") as ficheiro:
			linhas = ficheiro.readlines()  # type: list[str]
			for i in range(0, len(linhas)):
				linha_separada = linhas[i].split(SEPARADOR_FICHEIRO_1)
				if linha_separada[0] == utilizador_ligado:
					linhas[i] = utilizador_ligado + SEPARADOR_FICHEIRO_1 + nova_passe + SEPARADOR_FICHEIRO_2
					with open("utilizadores.txt", "w") as ficheiro_2:
						ficheiro_2.writelines(linhas)
					print("Palavra-passe alterada com sucesso. A voltar em 3 segundos...")
					time.sleep(3)
					menuLogin()
	elif escolha == ESCOLHA_TERM_SESSAO:
		utilizador_ligado = ""
		print("Sessão terminada com sucesso. A voltar para o menu principal em 3 segundos...")
		time.sleep(3)
		menuPrincipal()
	else:
		os.system("cls")
		if escolha == ESCOLHA_CALC:
			calculadora.main()
			print("A sair da Calculadora em 3 segundos...")
		elif escolha == ESCOLHA_JOGO_GALO:
			jogoGalo.main()
			print("A sair do Jogo do Galo em 3 segundos...")
		elif escolha == ESCOLHA_CHAT_BOT:
			chatBot.main()
			print("A sair do Chat Bot em 3 segundos...")
		time.sleep(3)
		menuLogin()

menuPrincipal()
