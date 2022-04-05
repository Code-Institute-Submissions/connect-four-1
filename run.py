import os
import time
from pyfiglet import figlet_format

COLUMN_COUNT = 10
ROW_COUNT = 7
PLAYER_1 = ' \U0001F534 '  # unicode for red circle
PLAYER_2 = ' \U0001F7E1 '  # Unicode for yellow circle

def cls():
    """
    Clear the console
    """
    os.system("cls" if os.name == "nt" else "clear")

def welcome_message():
    pass

def rules_screen():
    pass

def main_menu():
    pass

class GameBoard():
    """
    Declares a string to self.board
    Function print_board() prints the current game board
    """

    def __init__(self, turn):
        self.board = [['   ' for i in range(COLUMN_COUNT)]
                      for j in range(ROW_COUNT)]
        self.turn = turn

    def print_board(self):
        '''
        Prints the current game board
        With the corresponding column numbers at the top
        For easy access for players
        '''
        # Prints the column numbers over the corresponding columns
        grid = ''
        for row in self.board:
            grid += '-' * 64 + '\n'
            for column in row:
                # for the number of rows print the same number of columns
                grid += f' ||{column}'
            # Need to add one more column to the result to create the number of columns
            grid += ' ||\n'
        grid += '-' * 64
        print(' ')
        print('    1 ', '   2 ', '   3  ', '  4  ', '  5  ', '  6  ', '  7  ',
              '  8  ', '  9  ', '  10')
        print(grid)

    def drop_player_piece(self, column, player):
        """
        Drops a piece into the Connect4 selected column
        Fills the position with the PLAYER piece
        """
        column = int(column)  # column value is interger
        # Checks that the number input is between 1 and 10
        if column <= 9 and column >= 0 or column is None:
            if self.board[0][column] == '   ':
                for row in range(ROW_COUNT - 1, -1, -1):
                    if self.board[row][column] == '   ':
                        if self.turn == 0:
                            cls()
                            self.board[row][column] = player
                            self.print_board()
                            self.turn += 1
                        else:
                            cls()
                            self.board[row][column] = player
                            self.print_board()
                            self.turn += 1
                            self.turn = self.turn % 2
                        break
            else:
                print(" Column full, please choose another column")
        else:
            print(' That is not a valid number, try again')

    def check_move(self, player: str):
        """
        Check the horizontal, vertical and diagonal lines for 4 in a row for a win
        """
        # Check horizontal lines
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT):
                if self.board[row][column] == player and self.board[row][column + 1] == player and self.board[row][column +2] == player and self.board[row][column +3] == player:
                    return True

        # Check the vertical lines
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - 3):
                if self.board[row][column] == player and self.board[row + 1][column] == player and self.board[row + 2][column] == player and self.board[row + 3][column] == player:
                    return True

        # Check the diagonal line win to the right
        # counting positively up the columns and rows each time
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT - 3):
                if self.board[row][column] == player and self.board[row + 1][column + 1] == player and self.board[row + 2][column + 2] == player and self.board[row + 3][column +3] == player:
                    return True

        # Check the diagonal line win to the left
        # counting negatively down the rows and counting positively up the rows each time
        for column in range(COLUMN_COUNT - 3):
            for row in range(3, ROW_COUNT):
                if self.board[row][column] == player and self.board[row - 1][column + 1] == player and self.board[row - 2][column +2] == player and self.board[row - 3][column +3] == player:
                    return True

    def check_tie(self):
        """
        Checks if all the spaces have been filled
        If so it returns True
        """
        for i in self.board:
            for j in i:
                if j == '   ':
                    return False
        return True

def run_game():
    """
    Starts the game and sets the turn value for Player 1 to start
    """
    game = GameBoard(0)
    game.print_board()  # Initial game board
    game_play = False

    while not game_play:
        try:
            if game.turn == 0:
                player_move = input(
                    f' Player 1 ({PLAYER_1} ) insert red disc in column (1-10): '
                )
                game.drop_player_piece(int(player_move) - 1, PLAYER_1)
                if game.check_move(PLAYER_1):
                    print('')
                    print(f'                    PLAYER 1 ({PLAYER_1} ) WINS!')
                    print('')
                    print('+', '-'*60, '+')
                    print(figlet_format(' Game Over!', font = "marquee"))
                    quit()
            else:

                player_move = input(
                    f'Player 2 ({PLAYER_2} ) insert yellow disc in column (1-10): '
                )
                game.drop_player_piece(int(player_move) - 1, PLAYER_2)
                if game.check_move(PLAYER_2):
                    print('')
                    print(f'                    PLAYER 2 ({PLAYER_2} ) WINS!')
                    print('')
                    print('+', '-'*60, '+')
                    print(figlet_format('Game Over!', font = "marquee"))
                    quit()

            if game.check_tie():
                print('')
                print('                          No winners')
                print('')
                print('+', '-'*60, '+')
                print(figlet_format(' Game Over!', font = "marquee"))
                quit()

        except ValueError:
            print(' That is not a number ... Please try again')

def play_again():
    pass

def high_scores():
    pass

if __name__ == '__main__':
    run_game()
    