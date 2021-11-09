import copy
import pygame

X_img = None
O_img = None
mouse_clicked = False

#AI class: corresponds to the AI that will play tic tac toe---------------------
#Uses minmax with the help of some rules to choose where to play
class AI:
    def __init__(self) -> None:
        self.rules = [self.rule_1, self.rule_2, self.rule_3, \
                      self.rule_4, self.rule_5, self.rule_6, \
                      self.rule_7, self.rule_8]

    def make_play(self, board):
        coord = self.minmax(board, -1, 8)[0]
        return coord

    def minmax(self, board, player, depth):
        winner = board.get_winner()
        best_value = [None, 100*player]
        
        if winner in (-1, 0, 1):
            return [None, -winner]
        if depth == 0:
            return [None, 0]

        next_player = -player
        empty_pos = board.get_empty_positions()

        if len(empty_pos) == 9:
            empty_pos = [(1,1)]
        if len(empty_pos) == 8:
            if board.is_empty_pos(1,1):
                empty_pos = [(1,1)]
            else:
                empty_pos = [(0,0)]

    
        for pos in empty_pos:
            new_board = copy.deepcopy(board)
            new_board.apply_move(pos, player)
            new_value = self.minmax(new_board, next_player, depth-1)
        
            if player == 1:
                if new_value[1] < best_value[1]:
                    best_value = [pos, new_value[1]]
            else:
                if new_value[1] > best_value[1]:
                    best_value = [pos, new_value[1]]
        return best_value

            
    
    #Play in a position that leads to a victory
    def rule_1(self, board):
        empty_positions = board.get_empty_positions()
        for empty_pos in empty_positions:
            if board.is_winning_pos(empty_pos):
                return str(empty_pos[0]) + ":" + str(empty_pos[1])
        return None
    
    #Play in a position that blocks the oponent victory
    def rule_2(self, board):
        empty_positions = board.get_empty_positions()
        for empty_pos in empty_positions:
            if board.is_winning_pos(empty_pos, player=1):
                return str(empty_pos[0]) + ":" + str(empty_pos[1])
        return None

    #Cause a fork. Two ways of winning
    def rule_3(self, board):
        pass

    #Block a fork. Force the player to not create a fork
    def rule_4(self, board):
        pass
    
    #Play in the center
    def rule_5(self, board):
        if board.is_empty_pos(1, 1):
            return "1:1"
        return None
    
    #Play in the opposite corner
    def rule_6(self, board):
        pass

    #Play in an empty corner
    def rule_7(self, board):
        for pos in [(0,0), (2,0), (0,2), (2,2)]:
            if board.is_empty_pos(pos[0], pos[1]):
                return str(pos[0]) + ":" + str(pos[1])
        return None

    #Play in an middle empty square in any of the four sides:
    def rule_8(self, board):
        for pos in [(1,0), (0,1), (2,1), (1,2)]:
            if board.is_empty_pos(pos[0], pos[1]):
                return str(pos[0]) + ":" + str(pos[1])
        return None

#-------------------------------------------------------------------------------





# Cell class: corresponds to each cell in the board-----------------------------
#  1: X
#  0: Empty
#  2: O
class Cell:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    def __eq__(self, cell) -> bool:
        return self.value == cell.getValue()
    
    def __str__(self) -> str:
        if self.value == 1:
            return " X "
        elif self.value == 0:
            return "   "
        return " O "
#-------------------------------------------------------------------------------


# Board class: corresponds to the tic-tac-toe board-----------------------------
class Board:
    def __init__(self, board=None):
        self.cells = []
        for i in range(3):
            self.cells.append([Cell(0), Cell(0), Cell(0)])
        if board != None:
            self.cells = list(board.get_cells())
    
    def get_cells(self):
        return self.cells
    
    def get_line(self, n):
        return self.cells[n]

    def get_column(self, n):
        return [self.cells[0][n], self.cells[1][n], self.cells[2][n]]
    
    def get_diagonal(self, n):
        if n == 0:
            return [self.cells[0][0], self.cells[1][1], self.cells[2][2]]
        return [self.cells[0][2], self.cells[1][1], self.cells[2][0]]
    
    def get_num_empty_pos(self):
        return len([cell for line in self.cells for cell in line if cell == Cell(0)])
    
    def is_empty_pos(self, column, line):
        return self.cells[line][column] == Cell(0)
    
    def get_empty_positions(self):
        return [(c, l) for l in range(3) for c in range(3) if self.is_empty_pos(c, l)]
    
    def apply_move(self, move, value):
        self.cells[move[1]][move[0]] = Cell(value)

    #Makes the move made by the AI
    def apply_interactive_move(self, mouse_x, mouse_y, w, h, player=1):
        block_x = w//3
        block_y = h//3

        x_coord = mouse_x // block_x
        y_coord = mouse_y // block_y
    
        self.apply_move((x_coord, y_coord), player)
    
    #Traverses all the columns, lines and diagonals in the board and returns the 
    #winner
    def get_winner(self):
        n_empty_pos = self.get_num_empty_pos()
        for i in range(3):
            line = self.get_line(i)
            column = self.get_column(i)

            if len(line) == line.count(line[0]) and line[0] != Cell(0):
                return line[0].getValue()
            if len(column) == column.count(column[0]) and column[0] != Cell(0):
                return column[0].getValue()
        
        for i in range(2):
            diagonal = self.get_diagonal(i)
            if len(diagonal) == diagonal.count(diagonal[0]) and diagonal[0] != Cell(0):
                return diagonal[0].getValue()
        
        if n_empty_pos == 0:
            return 0
        
        return None

    #Returns true if the position sent as argument is a winning position
    def is_winning_pos(self, pos, player=-1):
        line = list(self.get_line(pos[1]))
        col = list(self.get_column(pos[0]))

        line[pos[0]] = Cell(player)
        col[pos[1]] = Cell(player)

        if line.count(line[0]) == 3 or col.count(col[0]) == 3:
            return True

        diag0 = [(0,0), (1,1), (2,2)]
        diag1 = [(2,0), (1,1), (0,2)]
        if pos in diag0:
            diagonal = list(self.get_diagonal(0))
            empty_index = diag0.index(pos)
            diagonal[empty_index] = Cell(player)
            if diagonal.count(diagonal[empty_index]) == 3:
                return True
        
        if pos in diag1:
            diagonal = list(self.get_diagonal(1))
            empty_index = diag1.index(pos)
            diagonal[empty_index] = Cell(player)
            if diagonal.count(diagonal[empty_index]) == 3:
                return True
        
        return False

    #Draws the scene using pygame
    def draw(self, screen, w, h):
        y_offset = h // 3
        x_offset = w // 3
        pygame.draw.line(screen, (255, 255, 255), (0, y_offset), (w, y_offset), width=2)
        pygame.draw.line(screen, (255, 255, 255), (0, y_offset*2), (w, y_offset*2), width=2)
        pygame.draw.line(screen, (255, 255, 255), (x_offset, 0), (x_offset, h), width=2)
        pygame.draw.line(screen, (255, 255, 255), (x_offset*2, 0), (x_offset*2, h), width=2)

        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Cell(1):
                    screen.blit(X_img, (x_offset*j, y_offset*i))
                elif self.cells[i][j] == Cell(-1):
                    screen.blit(O_img, (x_offset*j, y_offset*i))

    def __str__(self) -> str:
        res = "   0   1   2\n"
        res += "0 " + str(self.cells[0][0]) + "|" + str(self.cells[0][1]) + "|" + str(self.cells[0][2]) + "\n"
        for i in range(1, 3):
            res += "  -----------\n"
            res += str(i) + " " + str(self.cells[i][0]) + "|" + str(self.cells[i][1]) + "|" + str(self.cells[i][2]) + "\n"
        return res
#-------------------------------------------------------------------------------


# TicTacToe class: represents the game itself-----------------------------------
# The player number corresponds to the cell number------------------------------
class TicTacToe:
    def __init__(self, n_players) -> None:
        self.board = Board()
        self.current_player = 1
        self.player1_method = self.choose_position_manual
        self.player_has_played = False

        if n_players == 2:
            self.player2_method = self.choose_position_manual
        elif n_players == 1:
            self.player2_method = self.choose_position_auto

    def game_finished(self):
        return self.board.get_winner()

    def print_winning_player(self, winner):
        if winner == 0:
            print("Draw")
        else:
            print("Player " + str(winner) + " wins!")
    
    #Verifies if position is a free or if its inside the board
    def validate_play(self, position):
        if not self.board.is_empty_pos(position[0], position[1]):
            return False
        return True
    
    #Verifies if position is a free or if its inside the board by the string
    def validate_play_str(self, position):
        if len(position) != 3 or position[1] != ":":
            return False
        if position.count(":") != 1 or position[0] not in ("0", "1", "2") or position[2] not in ("0", "1", "2"):
            return False
        line = eval(position.split(":")[1])
        column = eval(position.split(":")[0])

        return self.validate_play((column, line))

    #Functions that asks the player for a move
    def choose_position_manual(self):
        player = "1"
        if self.current_player == -1:
            player = "2"


        position = input("Player " + player + "(ex. col:line):")
        while not self.validate_play_str(position):
            print("Invalid play!")
            position = input("Player " + player + "(ex. col:line):")

        coordinates = position.split(":")
        return (eval(coordinates[0]), eval(coordinates[1]))
    
    #Function that chooses play automatically
    def choose_position_auto(self):
        bot = AI()
        position = bot.make_play(self.board)
        return (position[0], position[1])
    
    #Converts the mouse position into board position
    def convert_mouse_to_pos(self, mouse_x, mouse_y, w, h):
        block_x = w//3
        block_y = h//3

        x_coord = mouse_x // block_x
        y_coord = mouse_y // block_y
        return (x_coord, y_coord)

    #Allows both players (or player) to play until a winner is found or the 
    #game ends in a draw
    def play(self): 
        while self.game_finished() == None:
            print(self.board)

            move = None
            if self.current_player == 1:
                move = self.player1_method()
            else:
                move = self.player2_method()
            
            self.board.apply_move(move, self.current_player)

            self.current_player = -self.current_player
        winner = self.game_finished()
        self.print_winning_player(winner)
    
    #Allows game against the AI interactively (using pygame)
    def play_interactive_ai(self, screen, w, h):
        global mouse_clicked

        self.board.draw(screen, w, h)
        if self.current_player == 1:
            mouse_x, mouse_y = (0, 0)
            click = pygame.mouse.get_pressed()[0] and mouse_clicked
            if click:
                mouse_clicked = False
                mouse_x, mouse_y = pygame.mouse.get_pos()
                move = self.convert_mouse_to_pos(mouse_x, mouse_y, w, h)

                if self.validate_play(move):
                    self.board.apply_move(move, self.current_player)
                    self.board.draw(screen, w, h)
                    self.player_has_played = True
                
                winner = self.game_finished()
                if winner == 1:
                    print("Player 1 wins")
                    return True
                elif winner == 0:
                    print("Draw")
                    return True
            
            if self.player_has_played:
                self.current_player = -1
                self.player_has_played = False
        else:
            move = self.player2_method()
            self.board.apply_move(move, -1)
            winner = self.game_finished()
            if winner == -1:
                print("Player 2 wins")
                return True
            elif winner == 0:
                print("Draw")
                return True
            self.current_player = 1
        return False
    
    #Allows game against another player interactively (using pygame)
    def play_interactive_manual(self, screen, w, h):
        global mouse_clicked

        self.board.draw(screen, w, h)
        mouse_x, mouse_y = (0, 0)
        click = pygame.mouse.get_pressed()[0] and mouse_clicked
        if click:
            mouse_clicked = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            move = self.convert_mouse_to_pos(mouse_x, mouse_y, w, h)

            if self.validate_play(move):
                self.board.apply_move(move, self.current_player)
                self.board.draw(screen, w, h)
                self.player_has_played = True
            winner = self.game_finished()
            if winner == 1:
                print("Player 1 wins")
                return True
            elif winner == -1:
                print("Player 2 wins")
                return True
            elif winner == 0:
                print("Draw")
                return True
        
        if self.player_has_played:
            self.current_player = -self.current_player
            self.player_has_played = False

#-------------------------------------------------------------------------------

#Interactive mode---------------------------------------------------------------
def open_interactive_game(mode=1):
    pygame.init()
    pygame.display.set_caption("Tic-Tac-Toe")
    
    width = 500
    height = 500
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((width, height))

    global X_img
    global O_img

    X_img = pygame.image.load("images/x.png")
    O_img = pygame.image.load("images/blue-circle.png")

    X_img = pygame.transform.scale(X_img, (width//3, height//3))
    O_img = pygame.transform.scale(O_img, (width//3, height//3))

    game = TicTacToe(mode)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        global mouse_clicked
        result = False
        if mode == 1:
            result = game.play_interactive_ai(screen, width, height)
        else:
            result = game.play_interactive_manual(screen, width, height)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = False
        
        if result:
            pygame.quit()
            running = False
            
        if running != False:
            pygame.display.update()
#-------------------------------------------------------------------------------



def play():
    game = None
    option = "-1"
    while option != "5":
        option = input("1 - vs Computer\n2 - 2 Players\n3 - Interactive vs Computer\n4 - Interactive 2 Players\n5 - Exit\n")
        if option == "1":
            game = TicTacToe(1)
            game.play()
        elif option == "2":
            game = TicTacToe(2)
            game.play()
        elif option == "3":
            open_interactive_game()
        elif option == "4":
            open_interactive_game(2)
        elif option == "5":
            return

        else:
            print("No valid option selected")

