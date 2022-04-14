import gspread
from google.oauth2.service_account import Credentials
import colorama
from termcolor import cprint
import visuals as vis
import run

colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Scope as defined in the Love Sandwiches
# Walk through project by Code Institute
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('connect4')

# Constant variables
USERNAME = SHEET.worksheet('usernames')
PLAYERS = ['Player 1', 'Player 2']


class UserData:
    """
    Sets the play_number with self.player_number
    Function create_username creates a username
    for the player_number passed in
    Function player_login logs the user in
    for the player_number passed in

    Attributes:
        player_number:
            Sets Player 1 or Player 2
    Methods:
        player_number:
            Sets Player 1 or Player 2
    """

    def __init__(self, player_number):
        self.player_number = player_number

    player1_total_losses = 0
    player1_total_wins = 0
    player1_wins = 0
    player1_losses = 0

    def create_username(self, player_number):
        """
        Creates a username for the player
        It calls the validate_player_name function
        to validate the user's input
        It checks if the users input
        has already been added to out google sheets

        Parameters:
            player_number:
                Sets Player1 or Player 2
                
            return:
                The current players user input - username
        """
        while True:
            # Player One creates username
            if player_number == 0:
                cprint(f"{PLAYERS[0]} please enter a username: ".center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                cprint(
                    "Note that any spaces in username input will be removed to make a single word "
                    .center(80),
                    run.COLORS['RED'],
                    attrs=['bold'])
            else:
                cprint(f"{PLAYERS[1]} please enter a username: ".center(80),
                       run.COLORS['YELLOW'],
                       attrs=['bold'])
                cprint(
                    "Note that any spaces in username input will be removed to make a single word "
                    .center(80),
                    run.COLORS['RED'],
                    attrs=['bold'])
            player_username = input().upper()
            player_username = player_username.strip()
            player_username = player_username.replace(' ', '')
            if validate_player_name(player_username):
                if player_username not in USERNAME.col_values(1):
                    run.cls()
                    vis.connect4_title()
                    if player_number == 0:
                        cprint(f"Hello {player_username} ...you are player 1 "
                               f"({run.PLAYER_1} )...".center(80),
                               run.COLORS['RED'],
                               attrs=['bold'])
                    else:
                        cprint(f"Hello {player_username} ...you are player 2 "
                               f"({run.PLAYER_2} )...".center(80),
                               run.COLORS['YELLOW'],
                               attrs=['bold'])
                    vis.blank_line()
                    loading = ".....Loading.....".center(80)
                    vis.typing_text(loading)
                    USERNAME.append_row([player_username, '0', '0'])
                    return player_username
                else:
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        'Username not available please pick another \n'.center(
                            80),
                        run.COLORS['RED'],
                        attrs=['bold'])
                    continue

    def player_login(self, player_number):
        """
        Checks if user input is already in google sheets
        and if not the error is handled
        Player 2's input also has to be checked
        Against the returned player 1 username
        So the same name cant be used twice to log in

        Parameters:
            player_number:
                Sets Player 1 or Player 2
        """
        while True:
            # Player inputs username
            if player_number == 0:
                cprint(
                    f"{PLAYERS[0]} please log in with your username: ".center(
                        80),
                    run.COLORS['RED'],
                    attrs=['bold'])
            else:
                cprint(
                    f"{PLAYERS[1]} please log in with your username: ".center(
                        80),
                    run.COLORS['YELLOW'],
                    attrs=['bold'])
            player_username = input().upper()
            if player_username in USERNAME.col_values(1):
                run.cls()
                vis.connect4_title()
                if player_number == 0:
                    cprint(
                        f'Welcome back {player_username}. You are {PLAYERS[0]}'
                        f' {run.PLAYER_1}'.center(80),
                        run.COLORS['RED'],
                        attrs=['bold'])
                else:
                    if player_username != player1_name:
                        cprint(
                            f'Welcome back {player_username}. You are {PLAYERS[1]}'
                            f' {run.PLAYER_2}'.center(80),
                            run.COLORS['YELLOW'],
                            attrs=['bold'])
                        vis.blank_line()
                        return player_username
                    else:
                        cprint('Username already logged in'.center(80),
                               run.COLORS['RED'],
                               attrs=['bold'])
                        vis.blank_line()
                        continue

                return player_username
            else:
                run.cls()
                vis.connect4_title()
                cprint('Cannot find username \n'.center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                continue


def validate_player_name(player):
    """
    Checks user input
    It strips any blank space from the username
    and checks to see if the username then has a value
    Also checks that the user input is between 3 and 10 characters long

    Parameters:
        player:
            player input from create_username function
    """
    try:
        if len(player) == 0:
            run.cls()
            vis.connect4_title()
            vis.blank_line()
            cprint(
                'Username cannot be blank, please enter a username \n'.center(
                    80),
                run.COLORS['RED'],
                attrs=['bold'])
            return False
        elif len(player) < 3 or len(player) > 10:
            run.cls()
            vis.connect4_title()
            vis.blank_line()
            cprint(
                'Username must be between 3 and 10 characters long \n'.center(
                    80),
                run.COLORS['RED'],
                attrs=['bold'])
            return False
        else:
            return True

    except ValueError:
        print('Error: please try again')
        return False


def get_user():
    """
    Sets the global variables
    It sets the user player_number for the Class
    Player one always starts first
    Depending on user input it calls either
    the create_username or player_login function
    It increments the player_number function
    And breaks the loop onces it reaches 2
    """

    global player1_name
    global player2_name
    global player1_wins
    global player1_losses
    global player1_data
    global player1_total_wins
    global player1_total_losses
    global player2_wins
    global player2_losses
    global player2_data
    global player2_total_losses
    global player2_total_wins
    player1_name = None
    player1_wins = 0
    player1_losses = 0
    player2_wins = 0
    player2_losses = 0

    player = UserData(0)  # Sets what player they are (1 or 2)

    while True:
        if player.player_number == 0:
            cprint(f'{PLAYERS[0]} \n'.center(80),
                   run.COLORS['RED'],
                   attrs=['bold'])
        else:
            cprint(f'{PLAYERS[1]} \n'.center(80),
                   run.COLORS['RED'],
                   attrs=['bold'])
        cprint('Press 1) Create username\n '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        cprint('Press 2) Login '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        menu_choice = input()

        if menu_choice == '1':
            # Player 1 creates username
            if player.player_number == 0:
                run.cls()
                vis.connect4_title()
                player1_name = player.create_username(0)
                player1_data = USERNAME.find(player1_name).row
                player1_total_wins = int(USERNAME.row_values(player1_data)[1])
                player1_total_losses = int(
                    USERNAME.row_values(player1_data)[2])
                player.player_number += 1
                run.cls()
                vis.connect4_title()

            else:
                # Player 2 creates username
                run.cls()
                vis.connect4_title()
                player2_name = player.create_username(1)
                player2_data = USERNAME.find(player2_name).row
                player2_total_wins = int(USERNAME.row_values(player2_data)[1])
                player2_total_losses = int(
                    USERNAME.row_values(player2_data)[2])
                player.player_number += 1

                if player.player_number == 2:
                    run.start_screen()

        elif menu_choice == '2':
            # Player 1 logs in
            if player.player_number == 0:
                run.cls()
                vis.connect4_title()
                player1_name = player.player_login(0)
                vis.blank_line()
                loading = ".....Loading.....".center(80)
                vis.typing_text(loading)
                player1_data = USERNAME.find(player1_name).row
                player1_total_wins = int(USERNAME.row_values(player1_data)[1])
                player1_total_losses = int(
                    USERNAME.row_values(player1_data)[2])
                player.player_number += 1
                run.cls()
                vis.connect4_title()

            else:
                # Player 2 logs in
                run.cls()
                vis.connect4_title()
                player2_name = player.player_login(1)
                loading = ".....Loading.....".center(80)
                vis.typing_text(loading)
                player2_data = USERNAME.find(player2_name).row
                player2_total_wins = int(USERNAME.row_values(player2_data)[1])
                player2_total_losses = int(
                    USERNAME.row_values(player2_data)[2])
                player.player_number += 1

                if player.player_number == 2:
                    run.start_screen()

        else:
            run.cls()
            vis.connect4_title()
            cprint('Please press 1 or 2 to make your choice \n'.center(80),
                   run.COLORS['RED'],
                   attrs=['bold'])
            continue


def cont_error(cont_input):
    """
    Function for error handling
    Press C to continue
    Making sure only C or c can be pressed

    Parameters:
        cont_input:
            user input
    """
    while cont_input not in ['c', 'C']:
        cprint('Please press C to continue...'.center(80),
               run.COLORS['RED'],
               attrs=['bold'])
        cont_input = input()
