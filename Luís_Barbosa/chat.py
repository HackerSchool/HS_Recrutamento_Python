# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:42:26 2021

@author: luis_
"""
import time 
import random
import datetime

def chat(utilizador):
    
    print(chr(27) + "[2J") # Limpa o terminal
    
    print("Bem vindo " + utilizador)                                # Imprime no terminal , "Bem-vindo xpto "
    
    cenas = str(input("Como posso ajudar ?:  "))
    
    while cenas == "" :
        #print(chr(27) + "[2J") # Limpa o terminal 
        time.sleep(0.5)
        cenas = str(input("Como posso ajudar ?  "))
        
       
        if cenas == "hackerschool" :                                # Resposta a uma palavra especifica (hackerschool)
               
            print("Desde 2012, a HackerSchool foca-se na criação de projetos nas mais diversas áreas da tecnologia, incentivando os seus membros a aprender e a colocar em prática o seu conhecimento em situações reais.")
           
            time.sleep(3)
        elif cenas == "horas" :                                     # Resposta a uma palavra especifica (horas)
        
            print(datetime.datetime.now())                          # Imprime as horas no momento , a partir do módulo datetime
            
            time.sleep(3)
            
           
        elif cenas != "hackerschool" or cenas != "horas" :
            
            
            with open("frases_aleatorias.txt") as f:                # Abrir o ficheiro "frases_aleatorias.txt" com se se chamasse f
                lines = f.read().splitlines()                       # Ler o ficheiro e separar por linhas
                print(random.choice(lines))                         # Escolher uma frase aleatória do ficheiro, recorrendo ao módulo Random
                    
            time.sleep(3)
    