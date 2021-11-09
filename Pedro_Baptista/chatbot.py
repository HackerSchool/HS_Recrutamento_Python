# Função com dois modos. No primeiro responde com strings random, no segundo procura por palavras chave
# para mandar essas mesmas frases de forma mais acertada
def chatbot():
    print('\nChatbot inicializado!\n')

    import random

    frases = ["Hoje está bom tempo!", "Concordo", "1+1=2", "Não sabia!", "Parabéns!", \
           "O Sol é uma estrela", "Obrigado!", "Está calor", "hum hum", "Eu também"]

    while 1:
        print('\nIndique o modo de funcionamento pretendido:\n4: Sistema de interação básico com respostas do bot totalmente aleatórias')
        print('5: Detetar na frase do utilizador palavras e mandar mensagens mais específicas\n')
        print('\nInseriu:')
        mode = input()
        print('\nSempre que desejar sair, responda com "1"')

        if mode == '4':

            print("Como se sente hoje?\n")

            while 1:
                scan = input()

                n = random.randint(0,9)
                answer = frases[n]

                print(answer,'\n')

                if scan == '1':
                    return

        if mode == '5':

            print("Como se sente hoje?\n")

            while 1:
                scan = input()

                if scan == '1':
                    print('Adeus!\n')
                    return

                if (scan.find('tempo') != -1):
                    answer = frases[0]
                elif (scan.find('fixe') != -1):
                    answer = frases[1]
                elif (scan.find('1+1') != -1):
                    answer = frases[2]
                elif (scan.find('gosto') != -1):
                    answer = frases[3]
                elif (scan.find('ganhei') != -1):
                    answer = frases[4]
                elif (scan.find('sol') != -1):
                    answer = frases[5]
                elif (scan.find('good bot') != -1):
                    answer = frases[6]
                elif (scan.find('temperatura') != -1):
                    answer = frases[7]
                elif (scan.find('bem') != -1):
                    answer = frases[9]
                else:
                        answer = frases[8]
                

                print(answer,'\n')

