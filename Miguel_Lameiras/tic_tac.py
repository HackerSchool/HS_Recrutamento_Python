from tkinter import *
import tkinter.font as tkFont
from random import *
from datetime import *

#Definir variavel global
botao = [None]*9
modo = 3 #Modo default de jogo - contra AI 
jogador = 'X'
numjogadas = 1

def mudar_modo(m): 
    global modo
    global jogador
    modo = m
    print("->Mudou modo de jogo:" + str(modo))
    reset()

def reset():
    global numjogadas
    for i in range(9):
        botao[i].config(text= ' ')
    numjogadas = 1
    print("->Reset jogo")

def getstate(t):
    texto = botao[t].cget('text')
    return texto
    
#Função para testar se alguem ganhou
def ganhou(t):
    #ver caso a caso, não é muito elegante mas não me apetece complicar
    if getstate(0) == 'X':
       if getstate(1) == 'X':
           if getstate(2) == 'X':
               if t:
                   return t
               else:   
                   temp = '0-1-2'
                   #print(temp)
                   return temp
       if getstate(3) == 'X':
           if getstate(6) == 'X':
                if t:
                   return t
                else:   
                   temp = '0-3-6'
                   #print(temp)
                   return temp
       if getstate(4) == 'X':
           if getstate(8) == 'X':
                if t:
                   return t
                else:   
                   temp = '0-4-8'
                   #print(temp)
                   return temp

    if getstate(0) == 'O':
       if getstate(1) == 'O':
           if getstate(2) == 'O':
               if t:
                   return t
               else:   
                   temp = '0-1-2'
                   #print(temp)
                   return temp
       if getstate(3) == 'O':
           if getstate(6) == 'O':
                if t:
                   return t
                else:   
                   temp = '0-3-6'
                   #print(temp)
                   return temp
       if getstate(4) == 'O':
           if getstate(8) == 'O':
                if t:
                   return t
                else:   
                   temp = '0-4-8'
                   #print(temp)
                   return temp

    if getstate(8) == 'X':
        if getstate(7) == 'X':
            if getstate(6) == 'X':
                if t:
                   return t
                else:
                    temp = '8-7-6'
                    #print(temp)
                    return temp
        if getstate(5) == 'X':
            if getstate(2) == 'X':
                if t:
                   return t
                else:
                    temp = '8-5-2'
                    #print(temp)
                    return temp

    if getstate(8) == 'O':
        if getstate(7) == 'O':
            if getstate(6) == 'O':
                if t:
                   return t
                else:
                    temp = '8-7-6'
                    #print(temp)
                    return temp
        if getstate(5) == 'O':
            if getstate(2) == 'O':
                if t:
                   return t
                else:
                    temp = '8-5-2'
                    #print(temp)
                    return temp

    if getstate(4) == 'X':
        if getstate(3) == 'X':
            if getstate(5) == 'X':
                if t:
                   return t
                else:
                    temp = '4-3-5'
                    #print(temp)
                    return temp
        if getstate(6) == 'X':
            if getstate(2) == 'X':
                if t:
                   return t
                else:
                    temp = '4-6-2'
                    #print(temp)
                    return temp
        if getstate(1) == 'X':
            if getstate(7) == 'X':
                if t:
                   return t
                else:
                    temp = '4-1-7'
                    #print(temp)
                    return temp
    
    if getstate(4) == 'O':
        if getstate(3) == 'O':
            if getstate(5) == 'O':
                if t:
                   return t
                else:
                    temp = '4-3-5'
                    #print(temp)
                    return temp
        if getstate(6) == 'O':
            if getstate(2) == 'O':
                if t:
                   return t
                else:
                    temp = '4-6-2'
                    #print(temp)
                    return temp 
        if getstate(1) == 'O':
            if getstate(7) == 'O':
                if t:
                   return t
                else:
                    temp = '4-1-7'
                    #print(temp)
                    return temp             
    else:
        return False

#definir proximo movimento AI do jogo
def proxmove():
    global numjogadas
    for i in range(9):
        if getstate(i) == ' ':
            #Jogada prioritaria para o AI, se pode ganhar ganha
            botao[i].config(text = 'O')
            if ganhou(True):
                return
            else:
                botao[i].config(text = ' ')
            #Se não pode ganhar a Ai, testar se pode impedir o jogador de ganhar na jogada seguinte
            botao[i].config(text = 'X')
            if ganhou(True):
                temp = ganhou(False)
                lido = [None]*3
                lido[0] = int(temp.split("-")[0])
                lido[1] = int(temp.split("-")[1])
                lido[2] = int(temp.split("-")[2])
                botao[i].config(text = ' ')
                for j in range(3):
                    if botao[lido[j]].cget('text') == ' ':
                        botao[lido[j]].config(text = 'O')
                return
            else:
                botao[i].config(text = ' ')
    #A segunda jogada do AI é critica, daí ter de prevenir duas situações
    if numjogadas == 3:
        #prevenir a jogada especifica que o jogador podia ganhar, sempre que jogador joga centro + canto, jogar canto
        if botao[4].cget('text') != 'X' or (botao[0].cget('text') == 'X' or botao[2].cget('text') == 'X' or botao[6].cget('text') == 'X' or botao[8].cget('text') == 'X'):
            aleat = randint(0,8)
            while botao[aleat].cget('text') == 'X' or botao[aleat].cget('text') == 'O' or (aleat != 0 and aleat != 2 and aleat != 6 and aleat != 8):
                aleat = randint(0,8)
            botao[aleat].config(text = 'O')
            return
            numjogadas = numjogadas + 2
        else:
            #prevenir a jogada especifica que o jogador podia ganhar, sempre que jogador joga canto + canto,não jogar canto
            numcantos = 0
            for i in range(9):
                if i == 0 or i == 2 or i == 6 or i == 8:
                    if botao[i].cget('text') == 'X':
                        numcantos = numcantos + 1
            if numcantos == 2:
                aleat = randint(0,8)
                while botao[aleat].cget('text') == 'X' or botao[aleat].cget('text') == 'O' or (aleat != 1 and aleat != 3 and aleat != 5 and aleat != 7):
                    aleat = randint(0,8)
                botao[aleat].config(text = 'O')
                return
                numjogadas = numjogadas + 2

    #jogada random do computador, computador joga para empatar caso não haja nenhuma jogada interessante a fazer
    aleat = randint(0,8)
    while botao[aleat].cget('text') == 'X' or botao[aleat].cget('text') == 'O':
        aleat = randint(0,8)
    botao[aleat].config(text = 'O')

def get_button(t):

    global modo #declarar que estou a usar uma variavel global 
    global jogador
    global numjogadas

    fontStyle = tkFont.Font(family="Lucida Grande", size=40)#Mudar o tamanho do texto sem mudar o tamanho do botao dá demasiado trabalho

    if modo == 1 :
        if getstate(t) == ' ' and numjogadas != 10: 
            botao[t].config(text = jogador)
            jogadortemp = jogador
            if jogador == 'X':
                jogador = 'O'
            else:
                jogador = 'X'
            if ganhou(True):
                window2=janelafim()
                msg = Label(window2, text = "Ganhou o jogador com: " + jogadortemp , font=fontStyle, bg='#6dba83' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                reset()
                window2.mainloop()
            numjogadas = numjogadas + 1
            if numjogadas == 10 :
                window2=janelafim()
                msg = Label(window2, text = "Empate!", font=fontStyle, bg='#667ead' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                reset()
                window2.mainloop()
                numjogadas = 1

    if modo == 2 :
        seed(datetime.now())
        if getstate(t) == ' ' and numjogadas <= 5: 
            botao[t].config(text = 'X')
            if ganhou(True):
                window2=janelafim()
                msg = Label(window2, text = "Ganhaste!", font=fontStyle, bg='#6dba83' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                reset()
                window2.mainloop()
            numjogadas = numjogadas + 1
            if numjogadas < 6:
                #jogada random do computador
                aleat = randint(0,8)
                while botao[aleat].cget('text') == 'X' or botao[aleat].cget('text') == 'O':
                    aleat = randint(0,8)
                botao[aleat].config(text = 'O')
                if ganhou(True):
                    window2=janelafim()
                    msg = Label(window2, text = "Ganhou o Computador!", font=fontStyle, bg='#c45b5b' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                    reset()
                    window2.mainloop()
        if numjogadas == 6:
            window2=janelafim()
            msg = Label(window2, text = "Empate!", font=fontStyle, bg='#667ead' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
            reset()
            window2.mainloop()
            numjogadas = 1

    if modo == 3 :
        if numjogadas == 9:
            if getstate(t) == ' ':
                botao[t].config(text = 'X')
                window2=janelafim()
                msg = Label(window2, text = "Empate!",font=fontStyle, bg='#667ead' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                reset()
                window2.mainloop()
                numjogadas = 1  
        else:
            if getstate(t) == ' ':
                botao[t].config(text = 'X')
                foi = False
                if numjogadas == 1:
                    #se jogador joga meio, jogar canto
                    if botao[4].cget('text') == 'X':
                        aleat = randint(0,8)
                        while aleat != 0 and aleat != 2 and aleat != 6 and aleat != 8:
                            aleat = randint(0,8)
                        botao[aleat].config(text = 'O')
                    #se jogador não joga meio, jogar meio
                    if botao[4].cget('text') == ' ' :
                        botao[4].config(text = 'O')
                    numjogadas = numjogadas + 2
                    foi = True
                if numjogadas != 1 and foi == False:
                    if ganhou(True):
                        #Teoricamente este if nem devia cá estar
                        window2=janelafim()
                        msg = Label(window2, text = "Ganhaste!", font=fontStyle, bg='#6dba83' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                        reset()
                        window2.mainloop()
                    else:
                        proxmove()
                        if ganhou(True):
                            window2=janelafim()
                            msg = Label(window2, text = "Ganhou o Computador!", font=fontStyle,bg='#c45b5b' , fg='#ffffff').place(relx=.5, y = 20, anchor="center") 
                            reset()
                            window2.mainloop()
                        numjogadas = numjogadas + 2 
def janelafim():

    print("\n->Fim do jogo")
    window2 = Tk()
    window2.title("Fim do Jogo")
    window2.geometry('200x100')
    positionRight = int(window2.winfo_screenwidth()/2 - 200/2)
    positionDown = int(window2.winfo_screenheight()/2 - 100/2)
    window2.geometry("+{}+{}".format(positionRight, positionDown))

    fontStyle = tkFont.Font(family="Lucida Grande", size=40)

    #imprimir resultado do jogo no fim
    temp = [None]*9
    for i in range(9):
        temp[i] = getstate(i)
        if temp[i] == ' ':
            temp[i] = '_'

    #msg1 = Label(window2, text = "Resultado:", bg='#2f2f2f' , fg='#6dba83').place(relx=.5, y = 25, anchor="center")
    msg2 = Label(window2, text = temp[0] + "|" + temp[1] + "|" + temp[2] + "\n" +
                                 temp[3] + "|" + temp[4] + "|" + temp[5] + "\n" +
                                 temp[6] + "|" + temp[7] + "|" + temp[8] , font = fontStyle ).place(relx=.5, y = 60, anchor="center")
    # botaofim = Button(window2, text = 'Reset',  command=reset())
    # botaofim.config(width = 5, height = 2,relief="raised", bg ='#479459')
    # botaofim.grid(row = 2 , column = 2)
    print("->Gerou janela->Fim do jogo")
    return window2
                                
def jogar():

    window = Tk()
    window.title("Jogo do Galo")
    window.geometry('300x270')
    positionRight = int(window.winfo_screenwidth()/2 - 300/2)
    positionDown = int(window.winfo_screenheight()/2 - 270/2)
    window.geometry("+{}+{}".format(positionRight, positionDown))
    window.config(bg='#2f2f2f')


    #criar menu bar
    menubar = Menu(window)
    new_item = Menu(menubar, tearoff=0)
    new_item.add_command(label='Jogador vs Jogador', command= lambda t = 1: mudar_modo(t))
    new_item.add_command(label='Jogador vs AI Random', command=  lambda t = 2: mudar_modo(t))
    new_item.add_command(label='Jogador vs AI Inteligente', command=  lambda t = 3: mudar_modo(t))
    menubar.add_cascade(label='Opções', menu=new_item)
    window.config(menu=menubar)
    print("\n->Gerou janela")

    #criar os botoes do jogo
    for i in range(9):
        botao[i] = Button(window, text = ' ' , command= lambda t = i : get_button(t))
        botao[i].config(width = 11, height = 6,relief="raised", bg ='#6dba83')#cor oficial da hackerschool ig
        if i < 3:
           botao[i].grid(row = 0 , column = i)
        if i > 2 and i < 6:
            botao[i].grid(row = 1 , column = i - 3)
        if i > 5:
            botao[i].grid(row = 2 , column = i - 6)
    print("->Gerou botao")
    
    window.mainloop()
