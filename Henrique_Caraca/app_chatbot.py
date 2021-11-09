# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:05:08 2021

@author: User
"""

from random import randrange

def chatbot1():
    # dá return de uma pessoa e uma ação pseudo aleatoriamente tendo em conta o input 
    pessoas=["O João", "O Homem-Aranha", "O Michael Jordan", "O Presidente", "A Maria"]
    verbo=["é fixe", "ficou maluco", "foi à praia", "joga futebol", "saltou de paraquedas"]
    a = input('Olá!\n')
    print(pessoas[(len(a)//2)%5],verbo[len(set(a))%5])
    
#chatbot1()

def chatbot2():
    
    # tenta detetar um tema por umas keywordse e dá uma respotsa/pergunta sobre esse tema
    
    temas=['no tempo', 'em desporto' , 'no mundo','em comida']
    '''
    tempo = ['Vai chover amanhã?', "Amanhã vai estar sol", "Hoje está calor"]
    tempo_key = ['tempo','sol','chuva','calor']
    desporto = ['Viste o jogo ontem?', 'Qual é o teu jogador favorito?','Eu gosto de jogar futebol']
    desporto_key = ['desporto','jogo','bola','futebol']
    mundo = ['Fun fact: existem 195 países', 'Que país gostavas de visitar?', 'Onde é que moras?']
    mundo_key = ['mundo', 'pais','paises','portugal','viajar']
    comida = ['Qual é a tua comida favorita?', 'Eu gosto de hamburgueres', 'O que é que vais jantar?']
    comida_key = ['comida','comer','fome','comi']
    '''
    
    keys = ['tempo','sol','chuva','calor',\
            'desporto','jogo','bola','futebol',\
            'mundo', 'pais','portugal','viajar',\
            'comida','comer','fome','comi']
    
    answer = ['Vai chover amanhã?', "Amanhã vai estar sol", "Hoje está calor",\
              'Viste o jogo ontem?', 'Qual é o teu jogador favorito?','Eu gosto de jogar futebol',\
              'Fun fact: existem 195 países', 'Que país gostavas de visitar?', 'Onde é que moras?',\
              'Qual é a tua comida favorita?', 'Eu gosto de hamburgueres', 'O que é que vais jantar?']
        
    a = input('Olá!\n')
    for word in a.split(' '):
        for i in range(len(keys)):
            if keys[i]==word:
                #print(i)
                print(f'Por falar {temas[i//4]}. {answer[(i//4)*3 + randrange(0,3)]}')
                return
    print('Não sei bem como responder, desculpa')


def main_cb():
    print("Bem-vindo à calculadora\n")
    while True:
        print('''\nEscolhe a tua opção:
              1 - Chat Bot Aleatorio
              2 - Chat Bot Simples
              q - Sair
              ''')
        opcao = input("Opção:\n")
        if opcao == '1':
            chatbot1()
        elif opcao == '2':
            chatbot2()
        elif opcao == 'q':
            print("A sair")
            break
        else:
            print("Opcao não válida")