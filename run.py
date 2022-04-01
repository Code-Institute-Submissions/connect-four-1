# Write your code to expect a terminal of 80 characters wide and 24 rows high

COLUMN_COUNT = 10
ROW_COUNT = 7
PLAYER_1 =  ' \U0001F534 '  # unicode for red circle
PLAYER_2 =  ' \U0001F7E1 '  # Unicode for yellow circle


class GameBoard():
    """
    Declares a string to self.board
    Function print_board() prints the current game board
    """

    def __init__(self):
        self.board = [['    ' for i in range(COLUMN_COUNT)]
                      for j in range(ROW_COUNT)]

    def print_board(self):
        '''
        Prints the current game board
        With the corresponding column numbers at the top
        For easy access for players
        '''
        # Prints the column numbers over the corresponding columns
        print('   0  ', ' 1  ', ' 2  ', ' 3  ', ' 4  ', ' 5  ', ' 6  ', ' 7  ', ' 8  ', ' 9',)
        grid = ''
        for row in self.board:
            grid += '-' * 62 + '\n'
            for column in row:
                grid += f'||{column}'  # for the number of rows print the same number of columns
            grid += '||\n'  # Need to add one more column to the result to create the number of columns
        grid += '-' * 62
        print(grid)

    def drop_player_piece(self, column, player: str):
        """
            
        """
        column = int(column) # column value is interger
        if column <= 8 and column >= 0 or column is None:
            if self.board[0][column] == '    ':
                for row in range(ROW_COUNT-1, -1, -1):  # Use -1, -1 as the top and bottom rows are not slots
                    if self.board[row][column] == '    ':
                        self.board[row][column] = player
                        break
            else:
                print('Column is full, please pick another column')
        else:
            print('Please pick a number 0 - 9')
    
    def check_move(self, player: str):
        pass


def run_game():
    game = GameBoard()
    game.print_board()

    while not game.check_move(PLAYER_1) and not game.check_move(PLAYER_2):
        column = input(f'Player 1 ({PLAYER_1}) insert piece in col (0-9): ')
        game.drop_player_piece(column, PLAYER_1)
        game.print_board()

        column = input(f'Player 2 ({PLAYER_2}) insert piece in col (0-9): ')
        game.drop_player_piece(column, PLAYER_2)
        game.print_board()


if __name__ == '__main__':
    run_game()