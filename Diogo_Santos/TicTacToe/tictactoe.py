from user import User
import random

class Tictactoe:
    ''' The core of the app tictactoe

    Attributes:
        user                The user in app
        botMark             The string corresponding to the bot mark in board
        playerMark          The string corresponding to the player mark in board
        blankMark           The string corresponding to a blank space in board
        count               The number of moves
        gameOver            The status of the game
        smart               The settings of the AI
        board               The board as matrix of characters
        winningConditions   The possible winning combinations

    This app allows the user to play game of tictactoe against a 
    random AI or an AI using the minimax algorithm.
    Visually, the player will always be the 'X' and the bot 'O'
    '''

    def __init__(self, user: User) -> None:
        ''' Creates an instance of the class Tictactoe '''
        self.user = user

        self.botMark = "O"
        self.playerMark = "X"
        self.blankMark = " "

        self.count = 0
        self.gameOver = True
        self.smart = True

        self.board = [" " for _ in range(9)]
        self.winningConditions = [
            [0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],
            [1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]

    
    def startGame(self, smart: bool) -> None:
        ''' Starts game and controls main game loop '''

        print("How to play:\nEnter a number between 1 and 9")
        print(f"{self.user.getName()}: X  VS  AI: O")

        self.smart = smart
        self.__resetGame()
        self.__printBoard()

        if random.randint(1, 2) == 1:
            print(f"It is {self.user.getName()}'s turn.")
            self.__userTurn()
        else:
            print("It is AI's turn.")

        while not self.gameOver:
            self.__botTurn()
            if(self.gameOver):
                break
            self.__userTurn()


    def __botTurn(self) -> None:
        ''' Plays the bot turn '''

        if(self.smart):
            self.__generateMove()
        else:
            self.__randomMove()

        self.count+=1
        self.__printBoard()

        if (self.__checkWinner() == self.botMark):
            self.gameOver = True

        if self.gameOver :
            print("AI wins!")
        elif self.count >= 9:
            self.gameOver = True
            print("It's a tie!")

        if not self.gameOver:
            print(f"It is {self.user.getName()}'s turn.")


    def __userTurn(self) -> None:
        ''' Process user turn '''

        while True:
            try:
                move = int(input("Move: "))
            except ValueError:
                print("Be sure to choose an integer between 1 and 9 (inclusive) and in an unmarked tile.")
                continue
        
            if (move not in [1,2,3,4,5,6,7,8,9] or self.board[move-1] != " "):
                print("Be sure to choose an integer between 1 and 9 (inclusive) and in an unmarked tile.")
                continue
            else:
                break

        self.board[move - 1] = self.playerMark
        self.count += 1
        self.__printBoard()

        if(self.__checkWinner() == self.playerMark):
            self.gameOver = True
        
        if self.gameOver:
            print(f"{self.user.getName()} wins!")
        elif self.count >= 9:
            self.gameOver = True
            print("It's a tie!")

        if not self.gameOver:
            print("It's AI's turn.")

    
    def __generateMove(self) -> None:
        ''' Calculates best move for the AI '''

        bestScore = -100

        for i in range(len(self.board)):
            # For each valid move, check best score
            if self.board[i] == self.blankMark:

                self.board[i] = self.botMark
                score = self.minimax(False)
                self.board[i] = self.blankMark

                if(score > bestScore):
                    bestScore = score
                    bestMove = i

        self.board[bestMove] = self.botMark


    def minimax(self, isMaximizing: bool) -> int:
        ''' Applies the minimax algorithm '''

        scores = {"X":-1, "O":1, "draw":0}
        result = self.__checkWinner()

        # Terminal call
        if(result != None):
            return scores[result]

        if (isMaximizing):
            bestScore = -100
            for i in range(len(self.board)):
               if(self.board[i] == self.blankMark):

                   self.board[i] = self.botMark
                   score = self.minimax(False)
                   self.board[i] = self.blankMark

                   if(score > bestScore):
                       bestScore = score

            return bestScore
        
        else:
            bestScore = 100
            for i in range(len(self.board)):
               if(self.board[i] == self.blankMark):

                   self.board[i] = self.playerMark
                   score = self.minimax(True)
                   self.board[i] = self.blankMark

                   if(score < bestScore):
                       bestScore = score

            return bestScore

    
    def __randomMove(self) -> None:
        ''' Generates a random move for the AI '''
        move = random.randint(0,8)
        while self.board[move] != self.blankMark:
            move = random.randint(0,9)

        self.board[move] = self.botMark


    def __checkWinner(self) -> str:
        ''' Checks if anyone has won '''

        draw = 0
        for i in range(len(self.board)):
            if(self.board[i] != " "):
                draw += 1

        if(draw == 9):
            return "draw"

        for mark in ['X','O']:
            for condition in self.winningConditions:
                if self.board[condition[0]] == mark and self.board[condition[1]] == mark and self.board[condition[2]] == mark:
                    return mark

        return None


    def __resetGame(self) -> None:
        ''' Resets game and relevant attributes '''

        self.gameOver = False
        self.count = 0
        self.board = [" " for _ in range(9)]


    def __printBoard(self) -> None:
        ''' Prints a string representation of the board '''
        
        board = "-------\n"
        for x in range(len(self.board)):
            board += "|"
            board += self.board[x]
            if x == 2 or x == 5 or x == 8:
                board  = board + ("|\n" + "-"*7 + "\n")
        print(board)