import login_functions
import Calculator_functions
import time
    
def main():

    menu_opt = login_functions.menu(0)                                            #Primeiro menu (Login/registar/sair)

    while(menu_opt != '3'):

        if(menu_opt == '1'):                                      #Opçao de login
            verif = login_functions.login()
            while(verif != '0'):                             #Autenticação aceite => verif = username

                login_opt = login_functions.menu(1)                                #Segundo menu (Calculadora/Tic-Tac-Toe/Mudar_pass/Logout)
                while(login_opt != '3'):   

                    if(login_opt == '1'):
                        Calculator_functions.calculadora_nvl5()
                    else:
                        login_functions.mudar_pass(verif)                      
                    login_opt = login_functions.menu(1)                            #Retorno ao menu secundário
                else:                                         #Logout
                    print("\nLogout realizado em segurança.")
                    time.sleep(2)
                    verif = '0'
        else:                                                 #Opção de novo registo => corresponde a menu_opt = 2
            verif = login_functions.registar()

        menu_opt = login_functions.menu(0)                                        #Retorno ao menu principal
    else:
        print("\nCumprimentos à família")
    return

main()