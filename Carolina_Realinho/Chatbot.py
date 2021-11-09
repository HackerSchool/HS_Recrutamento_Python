# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:49:32 2021

@author: Carolina
"""

def chat_bot():
    print("\nBem vindo ao Chat Bot!\nConverse com o nosso bot Filomena.")
    
    '''
    O chat bot forma respostas aleatórias a partir de uma combinação aleatória 
    de opções de resposta.
    O utilizador pode introduzir qualquer mensagem.
    '''
    
    principio = ["Não sei como ", "Por vezes, ", "Há quem diga que ", "Se calhar, ",
                 "Pergunto-me se ", "Acho que ", "Um estudo do MIT afirmou que "]
    
    meio = ["a Diana é ", "um terramoto é ", "a paisagem deste lugar foi ",
            "a precessão dos equinócios é ", "eu fui ", "tu consegues ser ",
            "as gerberas florescem de uma forma "]
    
    fim = ["um pouco irritante.", "estonteante.", "bonita com a luz apropriada.",
           "circular.", "algo destruidor.", "culta e adulta, como a RTP2.",
           "algo melhor que o Preço Certo."]
    
    from random import randint
    
    continuar=True
    
    while continuar==True:
        
        valor_p = randint(0,6)
        valor_m = randint(0,6)
        valor_f = randint(0,6)
        
        input("\nUtilizador: ")
        print(f"Filomena: {principio[valor_p]}{meio[valor_m]}{fim[valor_f]}")
        
        continuar = input("\nPressione '0' para continuar a conversa. Qualquer outro para sair. ")
        
        if continuar!='0':
            continuar=False
            break
        else:
            continuar = True