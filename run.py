import os
import time
import sys
import cursor
from pyfiglet import figlet_format
from colorama import init, Fore, Style
from termcolor import cprint
from tabulate import tabulate
import visuals as vis
import validation as val

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

COLUMN_COUNT = 10
ROW_COUNT = 7
PLAYER_1 = " \U0001F534 "  # unicode for red circle
PLAYER_2 = " \U0001F7E1 "  # Unicode for yellow circle

COLORS = {
    "RED": "red",
    "BLUE": "blue",
    "YELLOW": "yellow",
    "BLUE_HL": "on_blue",
    "RED_HL": "on_red",
    "YELLOW_HL": "on_yellow",
    "WHITE": "white",
}


def cls():
    """
    Clears the console
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_message():
    """
    Prints off the initial welcome message and title
    and opens the welcome screen menu
    User's can navigate to next screen via user input
    """
    vis.connect4_title()
    cursor.hide()
    cprint("Welcome to Connect4 Command Line Interface Game".center(80),
           COLORS["BLUE"],
           attrs=['bold'])
    cprint(
        "Press Enter after you make your choice below to register your input".
        center(80),
        COLORS["BLUE"],
        attrs=["bold"])
    vis.blank_line()
    cprint("Press 1) To get started \n ".center(80),
           COLORS["YELLOW"],
           attrs=["bold"])
    cprint("Press 2) Game Rules ".center(80), COLORS["YELLOW"], attrs=["bold"])
    menu_choice = input()

    while menu_choice not in ("1", "2"):
        cls()
        vis.connect4_title()
        cprint(
            "Please press 1 or 2 to make your choice \n".center(80),
            COLORS["RED"],
            attrs=["bold"],
        )
        cprint("Press 1) To get started \n ".center(80),
               COLORS["YELLOW"],
               attrs=["bold"])
        cprint("Press 2) Game Rules \n ".center(80),
               COLORS["YELLOW"],
               attrs=["bold"])
        menu_choice = input()
        continue

    if menu_choice == "1":
        cls()
        vis.connect4_title()
        val.get_user()
    elif menu_choice == "2":
        cls()
        rules_screen()


def rules_screen():
    """
    Issues a series of print statements to the user
    explaining the rules of the game
    Once the rules are explained, the user can naviagte
    Back to the between different screens via
    user input
    """
    vis.blank_line()
    cprint(
        figlet_format("Game Rules", font="banner3-D", justify="center"),
        COLORS["RED"],
        attrs=["bold"],
    )
    vis.blank_line()
    cprint(
        "Connect 4 CLI is a two player game played on a singular device \n".
        center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "Each player either creates a new username ...\n".center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "Or logs in with a username previously made \n".center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "IMPORTANT! Remember the username you have created \n".center(80),
        COLORS["RED"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "Your scores will be attached to your username \n".center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        f"Player 1 will be assigned a red disc ({PLAYER_1} )"
        f"and Player 2 a yellow disc ({PLAYER_2} ) \n".center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "The goal of the game is to get 4 of your discs in a row \n".center(
            80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.5)
    cprint(
        "Either 4 horizontally, or vertically, or diagonally \n".center(80),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1.6)
    cprint("Have fun! \n".center(80), COLORS["YELLOW"], attrs=["bold"])
    time.sleep(1.6)
    cprint("Press C to continue... \n ".center(80),
           COLORS["BLUE"],
           attrs=["bold"])
    cont = input()
    # Input error handling
    val.cont_error(cont)
    cls()
    # Input choice for users to navigate to next screen
    vis.blank_line()
    cprint(
        figlet_format("Game Rules", font="banner3-D", justify="center"),
        COLORS["RED"],
        attrs=["bold"],
    )
    vis.blank_line()
    cprint("Press 1) To Welcome Screen \n ".center(80),
           COLORS["YELLOW"],
           attrs=["bold"])
    cprint("Press 2) To get started \n ".center(80),
           COLORS["YELLOW"],
           attrs=["bold"])
    menu_choice = input()

    while menu_choice not in ("1", "2"):
        cls()
        cprint(
            figlet_format("Game Rules", font="banner3-D", justify="center"),
            COLORS["RED"],
            attrs=["bold"],
        )
        cprint("Please press 1 or 2 to make your choice \n".center(80),
               COLORS["RED"])
        cprint("Press 1) To Welcome Screen\n ".center(80),
               COLORS["YELLOW"],
               attrs=["bold"])
        cprint("Press 2) Game Rules \n ".center(80),
               COLORS["YELLOW"],
               attrs=["bold"])
        menu_choice = input()
        continue

    if menu_choice == "1":
        cls()
        welcome_message()
    elif menu_choice == "2":
        cls()
        vis.connect4_title()
        val.get_user()


def start_screen():
    """
    This shows users a start screen message
    And allow users to start the game when they are ready
    via user input
    """
    cls()
    cprint(
        figlet_format(" Ready?", font="banner3-D", justify="center"),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    cprint(
        f"{val.player1_name}, {val.player2_name} are you ready? \n".center(80),
        COLORS["WHITE"],
        attrs=["bold"],
    )
    cprint("Please press C to continue...".center(80),
           COLORS["BLUE"],
           attrs=["bold"])
    cont = input()

    val.cont_error(cont)

    cprint("... 3...\n".center(80), COLORS["BLUE"], attrs=["bold"])
    time.sleep(1)
    cprint("... 2...\n".center(80), COLORS["RED"], attrs=["bold"])
    time.sleep(1)
    cprint("... 1...\n".center(80), COLORS["YELLOW"], attrs=["bold"])
    time.sleep(1)
    cls()
    cprint(
        figlet_format(" PLAY!", font="banner3-D", justify="center"),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    time.sleep(1)
    cls()
    run_game()


class GameBoard:
    """
    Declares a string to self.board
    Function print_board() prints the current game board
    
    Attributes:
        board:
            Declares a string to self.board
        turn:
            Sets players turn
    """

    def __init__(self, turn):
        self.board = [["   " for i in range(COLUMN_COUNT)]
                      for j in range(ROW_COUNT)]
        self.turn = turn

    def print_board(self):
        """
        Prints the current game board
        With the corresponding column numbers at the top
        For easy access for players
        """
        # Prints the column numbers over the corresponding columns
        grid = ""
        for row in self.board:
            grid += "     " + "-" * 71 + "\n"
            # Adds a spaced column at the begining
            # Pushing the board towards the center
            grid += "   "
            for column in row:
                # for the number of rows print the same number of columns
                grid += f"  ||{column}"
            # Need to add one more column to the result
            # To create the correct number of columns
            grid += " ||\n"
        grid += "     " + "-" * 71
        vis.game_bar()
        vis.blank_line()
        print(
            "      ",
            "  1  ",
            "   2  ",
            "   3  ",
            "   4  ",
            "   5  ",
            "   6  ",
            "   7  ",
            "   8  ",
            "   9  ",
            "  10  ",
        )
        cprint(grid, COLORS["BLUE"], attrs=["bold"])

    def drop_player_piece(self, column, player):
        """
        Drops a piece into the Connect4 selected column
        Fills the position with the PLAYER piece
        
        Parameters:
            column = column number of user input
            player = Player 1(0) or Player 2 (1)
        """
        column = int(column)
        # Checks that the number input is between 1 and 10
        if column <= 9 and column >= 0 or column is None:
            if self.board[0][column] == "   ":
                for row in range(ROW_COUNT - 1, -1, -1):
                    if self.board[row][column] == "   ":
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
                cls()
                self.print_board()
                cprint(
                    "Column full, please choose another column".center(80),
                    COLORS["RED"],
                    attrs=["bold"],
                )
                vis.blank_line()
        else:
            cls()
            self.print_board()
            cprint(
                " That is not a valid number, try again \n".center(80),
                COLORS["RED"],
                attrs=["bold"],
            )

    def check_move(self, player: str):
        """
        Check the horizontal, vertical and diagonal lines
        for 4 in a row for a win
        
        Return:
            True for win
        """
        # Source code for figuring out the winning moves
        # Can be found below
        # https://www.askpython.com/python/examples/connect-four-game
        # Check horizontal lines
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT):
                if (self.board[row][column] == player
                        and self.board[row][column + 1] == player
                        and self.board[row][column + 2] == player
                        and self.board[row][column + 3] == player):
                    return True

        # Check the vertical lines
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT - 3):
                if (self.board[row][column] == player
                        and self.board[row + 1][column] == player
                        and self.board[row + 2][column] == player
                        and self.board[row + 3][column] == player):
                    return True

        # Check the diagonal line win to the right
        # counting positively up the columns and rows each time
        for column in range(COLUMN_COUNT - 3):
            for row in range(ROW_COUNT - 3):
                if (self.board[row][column] == player
                        and self.board[row + 1][column + 1] == player
                        and self.board[row + 2][column + 2] == player
                        and self.board[row + 3][column + 3] == player):
                    return True

        # Check the diagonal line win to the left
        # counting negatively down the rows
        # counting positively up the rows each time
        for column in range(COLUMN_COUNT - 3):
            for row in range(3, ROW_COUNT):
                if (self.board[row][column] == player
                        and self.board[row - 1][column + 1] == player
                        and self.board[row - 2][column + 2] == player
                        and self.board[row - 3][column + 3] == player):
                    return True

    def check_tie(self):
        """
        Checks if all the spaces have been filled
        If so it returns True
        
        return:
            True for full board, False for space left
        """
        for i in self.board:
            for j in i:
                if j == "   ":
                    return False
        return True


def run_game():
    """
    Starts the game and sets the turn value for Player 1 to start
    Ends the game when the check_move function finds a win
    """
    game = GameBoard(0)  # Set the turn to 0
    game.print_board()  # Initial game board

    while True:
        try:
            # Player 1's turn
            if game.turn == 0:
                cprint(
                    f" Player 1 ({PLAYER_1} ) "
                    f"insert red disc in column (1-10): ".center(80),
                    COLORS["RED"],
                    attrs=["bold"],
                )
                player_move = input()
                game.drop_player_piece(int(player_move) - 1, PLAYER_1)
                # If player 1 wins
                if game.check_move(PLAYER_1):
                    # Update wins and losses
                    val.player1_wins += 1
                    val.player1_total_wins += 1
                    val.player2_total_losses += 1
                    val.player2_losses += 1
                    val.USERNAME.update_cell(val.player1_data, 2,
                                             val.player1_total_wins)
                    val.USERNAME.update_cell(val.player2_data, 3,
                                             val.player2_total_losses)
                    cls()
                    game.print_board()
                    vis.game_over_text(0)
                    vis.blank_line()
                    cprint(
                        "Please press C to continue...".center(80),
                        COLORS["BLUE"],
                        attrs=["bold"],
                    )
                    cont = input()
                    # Input error handling
                    val.cont_error(cont)
                    play_again()

            # Player 2's turn
            else:
                cprint(
                    f"Player 2 ({PLAYER_2} ) "
                    f"insert yellow disc in column (1-10): ".center(80),
                    COLORS["YELLOW"],
                    attrs=["bold"],
                )
                player_move = input()
                game.drop_player_piece(int(player_move) - 1, PLAYER_2)

                # If player 2 wins
                if game.check_move(PLAYER_2):
                    val.player2_wins += 1
                    val.player2_total_wins += 1
                    val.player1_total_losses += 1
                    val.player1_losses += 1
                    val.USERNAME.update_cell(val.player2_data, 2,
                                             val.player2_total_wins)
                    val.USERNAME.update_cell(val.player1_data, 3,
                                             val.player1_total_losses)
                    cls()
                    game.print_board()
                    vis.game_over_text(1)
                    vis.blank_line()
                    cprint(
                        "Please press C to continue...".center(80),
                        COLORS["BLUE"],
                        attrs=["bold"],
                    )
                    cont = input()
                    # Input error handling
                    val.cont_error(cont)
                    play_again()

            # If game is a tie
            if game.check_tie():
                vis.blank_line()
                cprint("No winners \n".center(80),
                       COLORS["RED"],
                       attrs=["bold"])
                print("+", "-" * 60, "+")
                vis.game_over_text(3)
                vis.blank_line()
                cprint(
                    "Please press C to continue...".center(80),
                    COLORS["BLUE"],
                    attrs=["bold"],
                )
                cont = input()

                # Input error handling
                val.cont_error(cont)
                play_again()

        except ValueError:
            cls()
            game.print_board()
            cprint(
                " That is not a number ... Please try again \n".center(80),
                COLORS["RED"],
                attrs=["bold"],
            )


def play_again():
    """
    User input gets the users choice
    From there run the appropriate function
    to direct the user to the next screen
    """
    cls()
    cprint(
        figlet_format(" Play?", font="banner3-D", justify="center"),
        COLORS["YELLOW"],
        attrs=["bold"],
    )
    cprint("What would you like to do? \n".center(80),
           COLORS["YELLOW"],
           attrs=["bold"])
    cprint("Press 1) To play again \n ".center(80),
           COLORS["BLUE"],
           attrs=["bold"])
    cprint(
        "Press 2) To go back to Welcome screen(reset players)\n ".center(80),
        COLORS["BLUE"],
        attrs=["bold"],
    )
    cprint(
        "Press 3) To see leaderboard and your scores\n".center(80),
        COLORS["BLUE"],
        attrs=["bold"],
    )
    cprint("Press 4) To exit game \n".center(80),
           COLORS["BLUE"],
           attrs=["bold"])

    options = input()

    while options not in ("1", "2", "3", "4"):
        cls()
        cprint(
            figlet_format(" Play?", font="banner3-D", justify="center"),
            COLORS["YELLOW"],
            attrs=["bold"],
        )
        cprint(
            "Please press 1, 2, 3, or 4 to make your choice \n".center(80),
            COLORS["RED"],
        )
        cprint("What would you like to do? \n".center(80),
               COLORS["YELLOW"],
               attrs=["bold"])
        cprint("Press 1) To play again \n ".center(80),
               COLORS["BLUE"],
               attrs=["bold"])
        cprint(
            "Press 2) To go back to Welcome screen(reset players)\n ".center(
                80),
            COLORS["BLUE"],
            attrs=["bold"],
        )
        cprint(
            "Press 3) To see leaderboard and your scores\n".center(80),
            COLORS["BLUE"],
            attrs=["bold"],
        )
        cprint("Press 4) To exit game \n".center(80),
               COLORS["BLUE"],
               attrs=["bold"])
        options = input()

    if options == "1":
        cls()
        vis.connect4_title()
        print(Style.BRIGHT + Fore.WHITE +
              "Starting a new game between".center(80))
        vis.blank_line()
        print(Style.BRIGHT + Fore.BLUE +
              f"{val.player1_name} vs {val.player2_name}".center(80))
        vis.blank_line()
        loading = ".....Loading.....".center(80)
        vis.typing_text(loading)
        start_screen()

    elif options == "2":
        time.sleep(1)
        cls()
        start_game()

    elif options == "3":
        high_scores()

    elif options == "4":
        cls()
        vis.connect4_title()
        cprint(
            "Thanks for playing! See you again soon!\n".center(80),
            COLORS["BLUE"],
            attrs=["bold"],
        )
        sys.exit()


def high_scores():
    """
    Prints out the values of the current players
    both for the current round of game and overall stats
    Pulls data from gspread connected google sheets
    and sorts it by the number of wins and desc order
    Tabulate puts the data into a table
    """

    cls()
    # Print User stats bar
    cprint(" ".center(80), COLORS["WHITE"], COLORS["BLUE_HL"])
    cprint(
        f"{val.player1_name}  wins: {val.player1_wins}  "
        f"Losses: {val.player1_losses}      "
        f"Total Overall Stats - wins: "
        f"{val.player1_total_wins}"
        f" Losses: {val.player1_total_losses}".center(80), COLORS["WHITE"],
        COLORS["BLUE_HL"])
    cprint(" ".center(80), COLORS["WHITE"], COLORS["BLUE_HL"])
    cprint(
        f" {val.player2_name}  wins: {val.player2_wins} "
        f"Losses: {val.player2_losses}       "
        f"Total Overall Stats- wins: {val.player2_total_wins}"
        f" Losses: {val.player2_total_losses}".center(80), COLORS["WHITE"],
        COLORS["BLUE_HL"])
    cprint(" ".center(80), COLORS["WHITE"], COLORS["BLUE_HL"])
    vis.blank_line()
    cprint(" Leaderboard Scores ".center(80), COLORS["WHITE"], COLORS["RED_HL"])
    # Prints table of top 3 overall stats
    # sort by column 2 which is number of wins
    val.USERNAME.sort((2, "des"))
    show_stats = val.USERNAME.get_all_values()
    table = tabulate(show_stats[0:6], tablefmt="fancy_grid")
    print(table)
    vis.blank_line()
    cprint(" Please press C to continue...",
           COLORS["BLUE"],
           attrs=["bold"])
    cont = input()
    # Input error handling
    val.cont_error(cont)
    play_again()


def start_game():
    """
    Loads the various functions in order to create the game
    """
    welcome_message()
    val.get_user()


if __name__ == "__main__":
    # Wrap in try and except to handle ctrl + c error
    try:
        cls()
        start_game()
    except KeyboardInterrupt:
        cls()
        vis.connect4_title()
        cprint("Player pressed ctrl + c to quit".center(80),
               COLORS["BLUE"],
               attrs=["bold"])
        vis.blank_line()
        cprint(
            "Press the Run Program button to play again. See you again soon!".
            center(80),
            COLORS["BLUE"],
            attrs=["bold"],
        )
        vis.blank_line()
        sys.exit()
