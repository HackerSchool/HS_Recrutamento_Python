import math
import os
import random


class TicTacToe:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.player = 1

    def menu(self):
        """
        Display the menu for the tic-tac-toe game
        :return:
        void
        """
        string = "Welcome to TicTacToe\n" + \
                 "Choose one of the following options:\n" + \
                 "v: To play versus another player\n" + \
                 "c: To play versus a random CPU\n" + \
                 "p: To play versus a smart CPU\n" + \
                 "q: to quit\n"

        self.page_clear()
        print(string)
        user_choice = input(">")
        if user_choice == "q":
            return
        elif user_choice == "v":
            self.game_player()
        elif user_choice == "c":
            self.game_random(random.randint(1, 2))
        elif user_choice == "p":
            self.game_perfect(random.randint(1, 2))

    def _board_string(self):
        """
        Generates a printable string of the current board state
        :return:
        string
            a printable tic-tac-toe board with the current game state
        """
        string = ""
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    string += " "
                elif self.board[x][y] == 1:
                    string += "X"
                else:
                    string += "O"
                if y < 2:
                    string += "|"
            string += "\n"
            if x < 2:
                string += "-----\n"
        return string

    def _play_move(self, x, y, player):
        """
        Plays a move on the board withouth overriding an already played piece
        :param x: row of the move position
        :param y: collum of the move position
        :param player: the value to fill in
        :return:
        bool
            whether the move was played or not
        """
        if self.board[x][y] == 0:
            self.board[x][y] = player
            return True
        return False

    def _check_winner(self):
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:  # check rows
                return self.board[i][0]
            if self.board[2][i] != 0 and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:  # check collumns
                return self.board[0][i]
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:  # check diagonal top left bottom right
            return self.board[1][1]
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:  # check diagonal bottom left top right
            return self.board[1][1]
        return 0

    def _board_is_full(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    return False
        return True

    @staticmethod
    def page_clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def player_swap(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def player_input(self):
        """
        :return:
        None if the player wants to quit otherwise returns a tuple with the move that was played
        """
        moves = self.possible_moves()
        while True:
            user_input = input(
                f"player {self.player}'s turn\nx for vertical y for horizontal starting at top left or q to quit\nx y >")
            if user_input == "q":
                return None
            try:
                x, y = user_input.split()
                x = int(x)
                y = int(y)
                move = (x, y)
                if move in moves:
                    return move
                else:
                    print("Invalid Input")
            except:
                print("Invalid Input")

    def game_player(self):
        self.page_clear()
        print(self._board_string())
        while not self._board_is_full():
            move = self.player_input()
            if move is None:
                return
            else:
                self._play_move(move[0], move[1], self.player)
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
            self.player_swap()
        if self._check_winner() != 0:
            print(f"PLAYER {self._check_winner()} WINS!!!")
        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()

    def possible_moves(self):
        moves = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == 0:
                    moves.append((x, y))
        return moves

    def move_random(self, player_cpu):
        moves = self.possible_moves()
        move = moves[random.randint(0, len(moves) - 1)]
        self._play_move(move[0], move[1], player_cpu)

    def game_random(self, player_cpu):
        if player_cpu == 1:
            player_human = 2
        else:
            player_human = 1
        self.page_clear()
        print(self._board_string())
        while not self._board_is_full():
            if self.player == player_human:
                move = self.player_input()
                if move is None:
                    return
                else:
                    self._play_move(move[0], move[1], self.player)
                self.page_clear()
                print(self._board_string())
            elif self.player == player_cpu:
                self.move_random(player_cpu)
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
            self.player_swap()
        if self._check_winner() == player_human:
            print("Player Won!!!")
        elif self._check_winner() == player_cpu:
            print("CPU WON!!!")
        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()

    def minmax(self, player_cpu, current_player):
        moves = self.possible_moves()
        winner = self._check_winner()
        # if the game ended we return based on wether the CPU won,tied or lost
        if winner != 0:
            if winner == player_cpu:
                return 1
            else:
                return -1
        if len(moves) == 0:
            return 0

        # if the game didn't end we dig down on all possible moves
        scores = []
        for move in moves:
            self._play_move(move[0], move[1], current_player)
            if current_player == 2:
                current_player = 1
            else:
                current_player = 2
            scores.append(self.minmax(player_cpu, current_player))
            if current_player == 2:
                current_player = 1
            else:
                current_player = 2
            self.board[move[0]][move[1]] = 0
        if current_player == player_cpu:  # we pick the best move the player that is currently playing can make and return the score based on that
            return max(scores)
        else:
            return min(scores)

    def move_best(self, player_cpu, player_human):
        best_score = - math.inf
        best_move = None
        for move in self.possible_moves():  # check the outcome for all possible moves
            self._play_move(move[0], move[1], player_cpu)
            score = self.minmax(player_cpu, player_human)
            self.board[move[0]][move[1]] = 0
            if score > best_score:  # keep track of the move with the best outcome
                best_score = score
                best_move = move
        self._play_move(best_move[0], best_move[1], player_cpu)  # play the  move that leads to the best outcome

    def game_perfect(self, player_cpu):
        if player_cpu == 1:
            player_human = 2
        else:
            player_human = 1
        self.page_clear()
        print(player_cpu)
        print(self._board_string())
        for turns in range(9):
            if self.player == player_human:
                move = self.player_input()
                if move is None:
                    return
                else:
                    self._play_move(move[0], move[1], self.player)
            elif self.player == player_cpu:
                self.move_best(player_cpu, player_human)
            self.player_swap()
            self.page_clear()
            print(self._board_string())
            if self._check_winner() != 0:
                break
        if self._check_winner() == player_human:
            print("Player Won!!!")
        elif self._check_winner() == player_cpu:
            print("CPU WON!!!")
        else:
            print(f"TIE!!")
        print("Press ENTER to quit")
        input()
