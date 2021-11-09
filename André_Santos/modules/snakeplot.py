import os
import random
try:
    import curses
except:
    os.system('pip install windows-curses')
    import curses
from curses import textpad
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import time

def sett():
    #FRANCISCO EU SEI QUE ISTO É PARVO E QUE ISTO NAO DEVIA ESTAR AQUI, MUITO MENOS DEVIA USAR A KEYWORD GLOBAL PARA FAZER ESTAS CENAS MAS EU ESCREVI TUDO SEM FUNCOES SO PARA VER O CONCEITO E AGORA NAO TENHO TEMPO DE ANDAR A VER O QUE É QUE TENHO DE ANDAR A ENVIAR E A RECEBER DAS FUNÇÕES, PEÇO DESCULPA PELA VONTA DE MORRER QUE POSSA TER PROPORCIONADO

    #--SET INITIAL VARS
    console = curses.initscr() #initialize
    screen_height, screen_width = console.getmaxyx()

    window = curses.newwin(screen_height-6, screen_width-6, 3, 3)
    window.keypad(True) #enable keypad
    curses.noecho() #turn off automatic echoing of keys to the screen
    curses.curs_set(0)
    window.nodelay(True)


    #LOAD MENU
    while window.getch() != 10:
        for y in range(1, window.getmaxyx()[0]-1):
            for x in range(1, window.getmaxyx()[1]-1):
                if random.choice([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) == 1:
                    window.addch(y, x, curses.LINES)
                else:
                    window.addch(y, x, ' ')

        window.addstr(int(window.getmaxyx()[0]/2), (int(window.getmaxyx()[1]/2)) - 12, 'Press ENTER To Start')

        curses.delay_output(600)

    #CLEAN BEFORE PLAY
    for y in range(1, window.getmaxyx()[0]-1):
        for x in range(1, window.getmaxyx()[1]-1):
            window.addch(y, x, ' ')


    #LETS PLAY
    #define initial movement direction
    move = KEY_RIGHT

    #generate random coordinates to first food
    food = [random.randint(1, window.getmaxyx()[0]-2),random.randint(1, window.getmaxyx()[1]-2)]
    window.addch(food[0], food[1], curses.ACS_PI)

    #generate random x and y coordinates for the snake head
    spawn_x = random.randint(7, window.getmaxyx()[1]-10)
    spawn_y = random.randint(1, window.getmaxyx()[0]-2)

    #build snake based on the head coordinates
    snake = [[spawn_y, spawn_x], [spawn_y, spawn_x-1], [spawn_y, spawn_x-2],[spawn_y, spawn_x-3],[spawn_y, spawn_x-4],[spawn_y, spawn_x-5],[spawn_y, spawn_x-6],[spawn_y, spawn_x-7],[spawn_y, spawn_x-8],[spawn_y, spawn_x-9],[spawn_y, spawn_x-10],[spawn_y, spawn_x-11],[spawn_y, spawn_x-12],[spawn_y, spawn_x-13], [spawn_y, spawn_x-14], [spawn_y, spawn_x-15],[spawn_y, spawn_x-16],[spawn_y, spawn_x-17],[spawn_y, spawn_x-18],[spawn_y, spawn_x-19],[spawn_y, spawn_x-20],[spawn_y, spawn_x-21],[spawn_y, spawn_x-22]]

    return window, food, snake

#DEFAULT CURRENT MOVE IS RIGHT (COULD BE CHANGED!)
def game(current_move='KEY_RIGHT'):
    window, food, snake = sett()
    #START SCORE
    score = 0
    while True:
        #REFRESH THE WINDOW AND GET ANY PRESSED KEY
        event = window.getch()

        #EXIT IF 'Q' IS PRESSED
        if event == 113:
            break
        else:
            event = ''

        #UPDATE SNAKE SPEED
        #window.timeout(int(140 - (len(snake)/5 + len(snake)/10)%120))
        window.timeout(10)


        ##MOVE FOOD
        if event == KEY_UP:
            new_food = [food[0]-1, food[1]]
            if new_food[0] > 0 and new_food not in snake:
                window.addch(food[0], food[1], ' ')
                food[0] -= 1

        elif event == KEY_DOWN:
            new_food = [food[0]+1, food[1]]
            if new_food[0] < window.getmaxyx()[0]-1 and new_food not in snake:
                window.addch(food[0], food[1], ' ')
                food[0] += 1

        elif event == KEY_RIGHT:
            new_food = [food[0], food[1]+1]
            if new_food[1] < window.getmaxyx()[1]-1 and new_food not in snake:
                window.addch(food[0], food[1], ' ')
                food[1] += 1

        elif event == KEY_LEFT:
            new_food = [food[0], food[1]-1]
            if new_food[1]-1 > 0 and new_food not in snake:
                window.addch(food[0], food[1], ' ')
                food[1] -= 1


        #CALCULATE RELATIVE DISTANCES, BETWEEN FOOD AND SNAKE HEAD
        distanceX = food[1] - snake[0][1]
        distanceY = food[0] - snake[0][0]


        #GET AVAILABLE MOVES
        available_moves = get_available_moves(current_move)

        #GET BEST MOVE
        best_move = get_best_move(window, snake, current_move=current_move, available=available_moves, dx=distanceX, dy=distanceY)


        #PLAY
        choosen = str(best_move).replace("259", "up").replace("260", "left").replace("261", "right").replace("258", "down")

        available_translated = []
        for i in available_moves:
            available_translated.append(str(i).replace('259', 'up').replace('260', 'left').replace('261', 'right').replace('258', 'down'))

        #CONSOLE-LOG THE DECISION MADE
        print(f'\n [DECISION]: state: {score}, available: {available_translated}, played: {choosen}]')

        #CREATE THE BEST HEAD
        best_head = [snake[0][0] + (best_move == KEY_DOWN and 1) + (best_move == KEY_UP and -1), snake[0][1] + (best_move == KEY_LEFT and -1) + (best_move == KEY_RIGHT and 1)]

        #CHECK IF HEAD IS IN THE BOARD AND IF IT IS TELEPORT IT
        final_head = teleport_snake_head(window,best_head)

        #UPDATE THE CURRENT MOVE
        current_move = best_move

        #Exit if snake runs over itself
        if check_if_killed(snake):
            print(f'\n [LOST]: State: {score}')
            break

        #INSERT HEAD
        snake.insert(0, final_head)


        # When snake eats the food
        if snake[0] == food:
            score += 1
            food = []
            food = generate_food(food, snake, window)
        else:
            last = snake.pop()
            window.addch(last[0], last[1], ' ')
            window.addch(food[0], food[1], curses.ACS_PI) # display the current food in the new position
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        #DRAW BORDER
        window.border(0)

        #DISPLAY DEBUG INFORMATION
        display(window, available=available_translated, choosen=choosen, score=score, dx=distanceX, dy=distanceY)

    curses.endwin() #close the window and end the game

def display(window, available=[], choosen='???', score=0, dx=0, dy=0):
    window.addstr(0, 2, f'| SCORE:{score} | DX:{dx} | DY:{dy} | AV:{available} | BEST:{choosen} |')

def get_available_moves(current_move):
    available_moves = [KEY_UP, KEY_LEFT, KEY_RIGHT, KEY_DOWN]

    if current_move == KEY_RIGHT:
        available_moves.remove(KEY_LEFT)
    elif current_move == KEY_LEFT:
        available_moves.remove(KEY_RIGHT)
    elif current_move == KEY_UP:
        available_moves.remove(KEY_DOWN)
    elif current_move == KEY_DOWN:
        available_moves.remove(KEY_UP)

    return available_moves

def get_best_move(window, snake, current_move='', available=[], dx=0, dy=0):
    #SET INITIAL BEST_MOVE
    best_move = current_move

    #PLAY DIAGONAL
    if abs(dy) > abs(dx):
        if dy == 0:
            if dx < 0: #fruta a esquerda
                if current_move != KEY_RIGHT:
                    best_move = KEY_LEFT
                else:
                    best_move = random.choice([KEY_DOWN, KEY_UP])
            else: #fruta a direita
                if current_move != KEY_LEFT:
                    best_move = KEY_RIGHT
                else:
                    best_move = random.choice([KEY_DOWN, KEY_UP])
        elif dy < 0: #fruta em cima
            if current_move != KEY_DOWN:
                best_move = KEY_UP
            else:
                best_move = random.choice([KEY_RIGHT, KEY_LEFT])
        else: #fruta em baixo
            if current_move != KEY_UP:
                best_move = KEY_DOWN
            else:
                best_move = random.choice([KEY_RIGHT, KEY_LEFT])

    else:
        if dx == 0:
            if dy < 0: #fruta em cima
                if current_move != KEY_DOWN:
                    best_move = KEY_UP
                else:
                    best_move = random.choice([KEY_RIGHT, KEY_LEFT])
            else: #fruta em baixo
                if current_move != KEY_UP:
                    best_move = KEY_DOWN
                else:
                    best_move = random.choice([KEY_RIGHT, KEY_LEFT])
        elif dx < 0: #fruta a esquerda
            if current_move != KEY_RIGHT:
                best_move = KEY_LEFT
            else:
                best_move = random.choice([KEY_DOWN, KEY_UP])
        else: #fruta a direita
            if current_move != KEY_LEFT:
                best_move = KEY_RIGHT
            else:
                best_move = random.choice([KEY_DOWN, KEY_UP])

    #CREATES THE NEW HEAD TO THAT MOVE
    fruit_move_head = [snake[0][0] + (best_move == KEY_DOWN and 1) + (best_move == KEY_UP and -1), snake[0][1] + (best_move == KEY_LEFT and -1) + (best_move == KEY_RIGHT and 1)]

    #COMO É OBVIO ISTO DEVIA SER FEITO COM RECURSAO PARA TER A PROFUNDIDADE MAXIMA ATE AO OBSTACULO MAS EU SOU AUTISTA E COISO (ALGEBRA)

    #IF THE FRUIT BEST MOVE HEAD IS A KILLABLE PLAY OR 6 CHUNKS AWAY FROM DIEING
    if fruit_move_head in snake or get_free_space(window, snake, move=best_move) < random.choice([3,4,5,6,7,8,9,10]):
        max_score = 0

        #SET INITIAL MOVE
        best_move = current_move

        for first_moves in available:
            father_score = 0
            #1GENERATION
            father_score += get_free_space(window, snake, first_moves)

            #2GENERATION
            second_available = get_available_moves(first_moves)
            for second_moves in second_available:
                father_score += get_free_space(window, snake, second_moves)

                #3GENERATION
                third_available = get_available_moves(second_moves)
                for third_moves in third_available:
                    father_score += get_free_space(window, snake, third_moves)

                    #4GENERATION
                    fourth_available = get_available_moves(third_moves)
                    for fourth_moves in fourth_available:
                        father_score += get_free_space(window, snake, fourth_moves)

                        #COMPARE SCORES
                        if father_score > max_score:
                            max_score = father_score
                            best_move = first_moves

    return best_move

def check_if_killed(snake):
    if snake[0] in snake[1:]:
        return True
    else:
        return False

def get_free_space(window, snake, move=''):
    alive = 0

    possible_head = [snake[0][0] + (move == KEY_DOWN and 1) + (move == KEY_UP and -1), snake[0][1] + (move == KEY_LEFT and -1) + (move == KEY_RIGHT and 1)]

    while possible_head not in snake and alive < (window.getmaxyx()[1] and window.getmaxyx()[0]): #se nao for instant death
        #after passing alive check adds 1 to alive state
        alive += 1

        possible_head = [possible_head[0] + (move == KEY_DOWN and 1) + (move == KEY_UP and -1), possible_head[1] + (move == KEY_LEFT and -1) + (move == KEY_RIGHT and 1)]

        #TELEPORT THE HEAD IF IN THE BOARD LINES
        possible_head = teleport_snake_head(window,head=possible_head)

    return alive

def teleport_snake_head(window,head=[]):
    #TELEPORT WHEN HITS WALLS
    if head[0] == 0:
        new_head = [window.getmaxyx()[0]-1, head[1]]
    elif head[0] == window.getmaxyx()[0]:
        new_head = [0, head[1]]
    elif head[1] == 0:
        new_head = [head[0], window.getmaxyx()[1]-1]
    elif head[1] == window.getmaxyx()[1]:
        new_head = [head[0], 0]
    else:
        new_head = head

    return new_head

def generate_food(food, snake, window):
    while food == []:
        # Generate coordinates for next food
        #generate random coordinates to first food
        food = [random.randint(1, window.getmaxyx()[0]-2),random.randint(1, window.getmaxyx()[1]-2)]
        if food in snake: food = []

    window.addch(food[0], food[1], curses.ACS_PI) #display the food

    return food
