import random

# Serve para imprimir o jogo no seu estado atual
def build(line1,line2,line3):
    fill = "---|---|---\n"
    print("\n" + line1 + fill + line2 + fill + line3)

# Serve para o AI realizar as suas jogadas
def place_AI(line1,line2,line3):
    pos = ['1','2','3']
    line = random.choice(pos)
    column = random.choice(pos)
    print("\nLinha: " + line)
    print("Coluna: " + column)

    if line == '1':
        if column == '1' and line1.split(' | ')[0] != " X" and line1.split(' | ')[0] != " O":
            line1 = line1.replace(line1.split(' | ')[0]," O",1)
        elif column == '2' and line1.split(' | ')[1] != "X" and line1.split(' | ')[1] != "O":
            line1 = line1.replace("|   |","| O |")
        elif column == '3' and line1.split(' | ')[2] != "X \n" and line1.split(' | ')[2] != "O \n":
            line1 = line1.replace(line1.split(' | ')[2],"O \n")
        else:
            lines = place_AI(line1,line2,line3)
            return lines

    elif line == '2':
        if column == '1' and line2.split(' | ')[0] != " X" and line2.split(' | ')[0] != " O":
            line2 = line2.replace(line2.split(' | ')[0]," O",1)
        elif column == '2' and line2.split(' | ')[1] != "X" and line2.split(' | ')[1] != "O":
            line2 = line2.replace("|   |","| O |")
        elif column == '3' and line2.split(' | ')[2] != "X \n" and line2.split(' | ')[2] != "O \n":
            line2 = line2.replace(line2.split(' | ')[2],"O \n")
        else:
            lines = place_AI(line1,line2,line3)
            return lines

    elif line == '3':
        if column == '1' and line3.split(' | ')[0] != " X" and line3.split(' | ')[0] != " O":
            line3 = line3.replace(line3.split(' | ')[0]," O",1)
        elif column == '2' and line3.split(' | ')[1] != "X" and line3.split(' | ')[1] != "O":
            line3 = line3.replace("|   |","| O |")
        elif column == '3' and line3.split(' | ')[2] != "X \n" and line1.split(' | ')[2] != "O \n":
            line3 = line3.replace(line3.split(' | ')[2],"O \n")
        else:
            lines = place_AI(line1,line2,line3)
            return lines
    
    # Array de Strings
    lines = [line1,line2,line3]
    return lines


# Serve para o Player 2 realizar as suas jogadas
def place_p2(line1,line2,line3):
    a = 0
    while a != 1:
        line = input("{1,2,3} Line: ")
        column = input("{1,2,3} Column: ")
        if line == '1' or line == '2' or line == '3':
            if column == '1' or column == '2' or column == '3':
                break
        print("\n<ERROR> Position does not exist, try again!\n")
    
    if line == '1':
        if column == '1' and line1.split(' | ')[0] != " X" and line1.split(' | ')[0] != " O":
            line1 = line1.replace(line1.split(' | ')[0]," O",1)
        elif column == '2' and line1.split(' | ')[1] != "X" and line1.split(' | ')[1] != "O":
            line1 = line1.replace("|   |","| O |")
            #line1 = line1.replace(line1.split(' | ')[1],"O") --------------> tentativa
        elif column == '3' and line1.split(' | ')[2] != "X \n" and line1.split(' | ')[2] != "O \n":
            line1 = line1.replace(line1.split(' | ')[2],"O \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p2(line1,line2,line3)
            return lines

    elif line == '2':
        if column == '1' and line2.split(' | ')[0] != " X" and line2.split(' | ')[0] != " O":
            line2 = line2.replace(line2.split(' | ')[0]," O",1)
        elif column == '2' and line2.split(' | ')[1] != "X" and line2.split(' | ')[1] != "O":
            line2 = line2.replace("|   |","| O |")
        elif column == '3' and line2.split(' | ')[2] != "X \n" and line2.split(' | ')[2] != "O \n":
            line2 = line2.replace(line2.split(' | ')[2],"O \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p2(line1,line2,line3)
            return lines

    elif line == '3':
        if column == '1' and line3.split(' | ')[0] != " X" and line3.split(' | ')[0] != " O":
            line3 = line3.replace(line3.split(' | ')[0]," O",1)
        elif column == '2' and line3.split(' | ')[1] != "X" and line3.split(' | ')[1] != "O":
            line3 = line3.replace("|   |","| O |")
        elif column == '3' and line3.split(' | ')[2] != "X \n" and line1.split(' | ')[2] != "O \n":
            line3 = line3.replace(line3.split(' | ')[2],"O \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p2(line1,line2,line3)
            return lines
    
    # Array de Strings
    lines = [line1,line2,line3]
    return lines


# Serve para o Player 1 realizar as suas jogadas
def place_p1(line1,line2,line3):
    a = 0
    while a != 1:
        line = input("{1,2,3} Line: ")
        column = input("{1,2,3} Column: ")
        if line == '1' or line == '2' or line == '3':
            if column == '1' or column == '2' or column == '3':
                break
        print("\n<ERROR> Position does not exist, try again!\n")

    if line == '1':
        if column == '1' and line1.split(' | ')[0] != " O" and line1.split(' | ')[0] != " X":
            line1 = line1.replace(line1.split(' | ')[0]," X",1)
        elif column == '2' and line1.split(' | ')[1] != "O" and line1.split(' | ')[1] != "X":
            line1 = line1.replace("|   |","| X |")
            #line1 = line1.replace(line1.split(' | ')[1],"X") --------------> tentativa
        elif column == '3' and line1.split(' | ')[2] != "O \n" and line1.split(' | ')[2] != "X \n":
            line1 = line1.replace(line1.split(' | ')[2],"X \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p1(line1,line2,line3)
            return lines

    elif line == '2':
        if column == '1' and line2.split(' | ')[0] != " O" and line2.split(' | ')[0] != " X":
            line2 = line2.replace(line2.split(' | ')[0]," X",1)
        elif column == '2' and line2.split(' | ')[1] != "O" and line2.split(' | ')[1] != "X":
            line2 = line2.replace("|   |","| X |")
        elif column == '3' and line2.split(' | ')[2] != "O \n" and line2.split(' | ')[2] != "X \n":
            line2 = line2.replace(line2.split(' | ')[2],"X \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p1(line1,line2,line3)
            return lines

    elif line == '3':
        if column == '1' and line3.split(' | ')[0] != " O" and line3.split(' | ')[0] != " X":
            line3 = line3.replace(line3.split(' | ')[0]," X",1)
        elif column == '2' and line3.split(' | ')[1] != "O" and line3.split(' | ')[1] != "X":
            line3 = line3.replace("|   |","| X |")
        elif column == '3' and line3.split(' | ')[2] != "O \n" and line3.split(' | ')[2] != "X \n":
            line3 = line3.replace(line3.split(' | ')[2],"X \n")
        else:
            print("\nINVALID MOVE - Please try again")
            build(line1,line2,line3)
            lines = place_p1(line1,line2,line3)
            return lines

    # Array de Strings
    lines = [line1,line2,line3]
    return lines


# Jogo do Player 1 contra o AI
def tictactoe_level_7():
    line1 = "   |   |   \n"
    line2 = "   |   |   \n"
    line3 = "   |   |   \n"    
    
    build(line1,line2,line3)
    turn = 1

    # Loop com as jogadas
    while turn < 6:
        print("~~~ TURN " + str(turn) + " ~~~\n")

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print("[X] Player 1, it's your turn!")

        lines = place_p1(line1,line2,line3)        
        line1 = lines[0]
        line2 = lines[1]
        line3 = lines[2]
        build(line1,line2,line3)

        # WIN CONDITIONS - PLAYER 1
        # All Lines
        if line1 == " X | X | X \n" or line2 == " X | X | X \n" or line3 == " X | X | X \n":
            print("Player 1 is the winner!!!\n")
            break
        # 1st Column
        elif line1.split(' | ')[0] == ' X' and line2.split(' | ')[0] == ' X' and line3.split(' | ')[0] == ' X':
            print("Player 1 is the winner!!!\n")
            break
        # 2nd Column
        elif line1.split(' | ')[1] == 'X' and line2.split(' | ')[1] == 'X' and line3.split(' | ')[1] == 'X':
            print("Player 1 is the winner!!!\n")
            break
        # 3rd Column
        elif line1.split(' | ')[2] == 'X \n' and line2.split(' | ')[2] == 'X \n' and line3.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break
        # 1st Diagonal
        elif line1.split(' | ')[0] == ' X' and line2.split(' | ')[1] == 'X' and line3.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break
        # 2nd Diagonal
        elif line3.split(' | ')[0] == ' X' and line2.split(' | ')[1] == 'X' and line1.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # DRAW CONDITION
        if turn == 5:
            print("It's a draw...\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print("[O] It's the AI's turn!")

        lines = place_AI(line1,line2,line3) 
        line1 = lines[0]
        line2 = lines[1]
        line3 = lines[2]
        build(line1,line2,line3)

        # WIN CONDITIONS - The AI
        # All Lines
        if line1 == " O | O | O \n" or line2 == " O | O | O \n" or line3 == " O | O | O \n":
            print("The AI is the winner!!!\n")
            break
        # 1st Column
        elif line1.split(' | ')[0] == ' O' and line2.split(' | ')[0] == ' O' and line3.split(' | ')[0] == ' O':
            print("The AI is the winner!!!\n")
            break
        # 2nd Column
        elif line1.split(' | ')[1] == 'O' and line2.split(' | ')[1] == 'O' and line3.split(' | ')[1] == 'O':
            print("The AI is the winner!!!\n")
            break
        # 3rd Column
        elif line1.split(' | ')[2] == 'O \n' and line2.split(' | ')[2] == 'O \n' and line3.split(' | ')[2] == 'O \n':
            print("The AI is the winner!!!\n")
            break
        # 1st Diagonal
        elif line1.split(' | ')[0] == ' O' and line2.split(' | ')[1] == 'O' and line3.split(' | ')[2] == 'O \n':
            print("The AI is the winner!!!\n")
            break
        # 2nd Diagonal
        elif line3.split(' | ')[0] == ' O' and line2.split(' | ')[1] == 'O' and line1.split(' | ')[2] == 'O \n':
            print("The AI is the winner!!!\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Incrementa o número de turnos até a condição de saída do loop 'while' ser atingida
        turn += 1

    # É dada a opção de realizar outro jogo
    choice = input("{y,n} Play another game? ")

    while choice != 'y' or choice != 'n':
        if choice == 'y':
            print("\nCreating a new game...\n")
            tictactoe()
            break
        elif choice == 'n':
            print("\nThank you for playing!\n")
            break
        else:
            print("\n<ERROR> Unknown Command\n")
            choice = input("{y,n} Play another game? ")
    return


# Jogo do Player 1 contra o Player 2
def tictactoe_level_5():
    line1 = "   |   |   \n"
    line2 = "   |   |   \n"
    line3 = "   |   |   \n"    
    
    build(line1,line2,line3)
    turn = 1

    # Loop com as jogadas e condições de vitória
    while turn < 6:
        print("~~~ TURN " + str(turn) + " ~~~\n")

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print("[X] Player 1, it's your turn!")

        lines = place_p1(line1,line2,line3)        
        line1 = lines[0]
        line2 = lines[1]
        line3 = lines[2]
        build(line1,line2,line3)

        # WIN CONDITIONS - Player 1
        # All Lines
        if line1 == " X | X | X \n" or line2 == " X | X | X \n" or line3 == " X | X | X \n":
            print("Player 1 is the winner!!!\n")
            break
        # 1st Column
        elif line1.split(' | ')[0] == ' X' and line2.split(' | ')[0] == ' X' and line3.split(' | ')[0] == ' X':
            print("Player 1 is the winner!!!\n")
            break
        # 2nd Column
        elif line1.split(' | ')[1] == 'X' and line2.split(' | ')[1] == 'X' and line3.split(' | ')[1] == 'X':
            print("Player 1 is the winner!!!\n")
            break
        # 3rd Column
        elif line1.split(' | ')[2] == 'X \n' and line2.split(' | ')[2] == 'X \n' and line3.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break
        # 1st Diagonal
        elif line1.split(' | ')[0] == ' X' and line2.split(' | ')[1] == 'X' and line3.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break
        # 2nd Diagonal
        elif line3.split(' | ')[0] == ' X' and line2.split(' | ')[1] == 'X' and line1.split(' | ')[2] == 'X \n':
            print("Player 1 is the winner!!!\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # DRAW CONDITION
        #É uma das condições de saída do loop 'while'
        if turn == 5:
            print("It's a draw...\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print("[O] Player 2, it's your turn!")

        lines = place_p2(line1,line2,line3) 
        line1 = lines[0]
        line2 = lines[1]
        line3 = lines[2]
        build(line1,line2,line3)

        # WIN CONDITIONS - Player 2
        # All Lines
        if line1 == " O | O | O \n" or line2 == " O | O | O \n" or line3 == " O | O | O \n":
            print("Player 2 is the winner!!!\n")
            break
        # 1st Column
        elif line1.split(' | ')[0] == ' O' and line2.split(' | ')[0] == ' O' and line3.split(' | ')[0] == ' O':
            print("Player 2 is the winner!!!\n")
            break
        # 2nd Column
        elif line1.split(' | ')[1] == 'O' and line2.split(' | ')[1] == 'O' and line3.split(' | ')[1] == 'O':
            print("Player 2 is the winner!!!\n")
            break
        # 3rd Column
        elif line1.split(' | ')[2] == 'O \n' and line2.split(' | ')[2] == 'O \n' and line3.split(' | ')[2] == 'O \n':
            print("Player 2 is the winner!!!\n")
            break
        # 1st Diagonal
        elif line1.split(' | ')[0] == ' O' and line2.split(' | ')[1] == 'O' and line3.split(' | ')[2] == 'O \n':
            print("Player 2 is the winner!!!\n")
            break
        # 2nd Diagonal
        elif line3.split(' | ')[0] == ' O' and line2.split(' | ')[1] == 'O' and line1.split(' | ')[2] == 'O \n':
            print("Player 2 is the winner!!!\n")
            break

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Incrementa o número de turnos até a condição de saída do loop 'while' ser atingida
        turn += 1


    # É dada a opção de realizar outro jogo
    choice = input("{y,n} Play another game? ")

    while choice != 'y' or choice != 'n':
        if choice == 'y':
            print("\nCreating a new game...\n")
            tictactoe()
            break
        elif choice == 'n':
            print("\nThank you for playing!")
            break
        else:
            print("\n<ERROR> Unknown Command\n")
            choice = input("{y,n} Play another game? ")
    return



def tictactoe():
    print("\n-------------------------\n|                       |\n|    · Tic-Tac-Toe ·    |\n|                       |\n|  1 - PvP (5)          |\n|                       |\n|  2 - Player v AI (7)  |\n|                       |\n|  3 - Login Menu       |\n|                       |\n-------------------------\n")
    option = input("Type the option's number: ")

    if option == '1':
        tictactoe_level_5()
        tictactoe()
        return
    elif option == '2':
        tictactoe_level_7()
        tictactoe()
        return
    elif option == '3':
        return
    else:
        print("\n<ERROR> Unknown Option\n")
        tictactoe()    
    return