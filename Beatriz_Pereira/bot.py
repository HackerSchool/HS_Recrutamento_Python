# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:17:08 2021

@author: beama
"""
import random as r

def botmain():
    print("Escolhe uma ação:\n 1-Interação com respostas aleatórias\n 2-Interação com respostas a identificar palavras no input\n")
    opcao=input("Ação:\n")
    if opcao=='1':
        botaleat()
    if opcao=='2':
        botident()
    else:
        return 0
    
    
def botaleat(): #funcao que da respostas aleatorias, p isso importou-se o modulo random
                #que escolhe um numero ao calhas entre o numero de respostas possiveis e 
                #responde a resposta correspondente a esse numero aleatorio
    input("Olá, eu sou um ChatBot. Conversa comigo\n")
    aleat=r.randint(0,4)
    if aleat==0:
        print("Hoje está sol lá fora")
    if aleat==1:
        print("Está tudo bem, e contigo?")
    if aleat==2:
        print("Hoje é sexta feira")
    if aleat==3:
        print("Fui criado no dia 03/11/2021")
    if aleat==4:
        print("Espero que tenhas um bom dia!")
        
def botident(): #esta funcao identifica palavras especificas na string do input e responde coisas a ver c essa palavra, ja nao e completamente aleatorio
    while True:
        strin=input("Olá, eu sou um ChatBot. Conversa comigo\n")
        listin=strin.split(' ')
        if 'tempo' in listin:
            print("Hoje está nublado!\n")
        if 'horas' in listin:
            print("São 12:46\n")
        if 'origem' in listin:
            print("Fui criado no dia 03/11/2021\n")
        if 'amigo' in listin:
            print("Sou teu amigo!\n")
        if 'bem' in listin:
            print("Está tudo bem, e contigo?")
        if 'música' in listin:
            print("Gosto de ouvir música portuguesa\n")
        if 'sair' in listin: #se ler a palavra sair para de pedir inputs e vai p o menu da aplicação
            break
        