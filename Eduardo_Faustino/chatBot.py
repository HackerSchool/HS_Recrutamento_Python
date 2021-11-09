# coding=utf-8
"""
O módulo Chat Bot.
"""
import random

import urllib.request
import html

def main():
	while True:
		frase = input("Enviar para o bot: ")  # type: str
		if "como" in frase and "está" in frase and "tempo" in frase:
			lista_palavras = []  # type: list[str]
			with open("respostas_aleatórias.txt", "r") as ficheiro:
				for linha in ficheiro.readlines():
					if "P / tempo /" in linha:
						lista_palavras.append(linha.split(' / ')[-1][:-1])

			frase = ""
			lista_respostas = []
			for char in fazerRequisicao("https://www.tempo.pt/lisboa.htm"):
				if char not in "<>":
					# Caracteres principais do HTML - parando ao encontrar um, penso que só fica pleno texto
					frase += char
				else:
					for i in ['chuva', 'sol', 'limpo', 'nublado']:
						if i in frase and "\\x" not in frase:
							lista_respostas.append(html.unescape(frase))
							break
					frase = ""

			resposta = ""
			for i in lista_respostas:
				if len(i.split()) > 1 and len(i) <= 15 and "=!\"#$%&/()=?":
					proximo = False
					for char in i:
						if char in "=!\"#$%&/()=?":
							proximo = True
							break
					if not proximo:
						resposta = i
						break

			print(f"Resposta: O tempo está {resposta}\n")

		if "como" in frase and "estás" in frase:
			resposta = ""  # type: str
			lista_palavras = []  # type: list[str]
			with open("respostas_aleatórias.txt", "r") as ficheiro:
				for linha in ficheiro.readlines():
					if "P / estado / " in linha:
						lista_palavras.append(linha.split(' / ')[-1][:-1])
					elif "F / estado / " in linha:
						resposta = linha.split(" / ")[-1][:-1]

			print(
				"Resposta: " + resposta.replace("[1]", lista_palavras[random.randrange(0, len(lista_palavras))]) + "\n")

		if frase == "sair":
			print("Ok, até um dia.")
			return


def fazerRequisicao(site: str) -> str:
	"""
	| Faz uma requisição simples a um site e retorna os conteúdos.

	:param site: o site ao qual fazer a requisição

	:return: a string dos conteúdos
	"""
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers = {'User-Agent': user_agent, }
	request = urllib.request.Request(site, headers=headers)
	response = urllib.request.urlopen(request)
	return str(response.read())
