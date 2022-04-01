# Write your code to expect a terminal of 80 characters wide and 24 rows high
COLUMN_COUNT = 10
ROW_COUNT = 7
 
#First code commit
class GameBoard():
    """
    Declares a string to self.board
    Function print_board() prints the current game board
    """
    def __init__(self):
        self.board = [['   ' for i in range(COLUMN_COUNT)]
                      for j in range(ROW_COUNT)]
 
    def print_board(self):
        '''
        Prints the current game board
        With the corresponding column numbers at the top
        For easy access for players
        '''
        # Prints the column numbers over the corresponding columns
        print('   1  ', ' 2  ', ' 3  ', ' 4  ', ' 5  ', ' 6  ', ' 7  ', ' 8  ', ' 9  ', ' 10', )
        grid = ''
        for row in self.board:
            grid += '-' * 52 + '\n'
            for column in row:
                grid += f'||{column}' # for the number of rows print the same number of columns
            grid += '||\n' # Need to add one more column to the result to create the number of columns
        grid += '-' * 52
        print(grid)
 
game = GameBoard()
game.print_board()

