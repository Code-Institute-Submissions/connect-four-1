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


def create_username(player, player_number):
    """
    This function takes the passed in argument from the Class
    If this parameter is = 0 it sets up Player One's username
    If this parameter is = 1 it sets up Player Two's username
    It calls the validate_player_name function
    To check that the username fills the proper criteria
    It checks if the player_name input
    Has already been added to out google sheets
    if so, it calls an error and prompting
    The user to pick a different username
    if not it adds the player_name input to the google sheets
    """
    while True:
        player1_username = None
        player2_username = None

        # Player One creates username
        if player_number == 0:
            cprint("Player 1 please enter a username: ".center(80),
                   run.COLORS['BLUE'],
                   attrs=['bold'])
            player = input()
            if validate_player_name(player):
                if player not in USERNAME.col_values(1):
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        f"Hello {player} ...you are player 1"
                        f"({run.PLAYER_1} )..."
                        .center(80),
                        run.COLORS['RED'],
                        attrs=['bold'])
                    vis.blank_line()
                    loading = ".....Loading.....".center(80)
                    vis.typing_text(loading)
                    # Converts the player input into an list item
                    # So it can be handled in google sheets
                    player1_username = player.split()
                    USERNAME.append_row(player1_username)

                else:
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        'Username not available please pick another \n'.center(
                            80),
                        run.COLORS['RED'],
                        attrs=['bold'])
                    continue
            else:
                continue
        else:
            # Player Two creates username
            cprint("Player 2 please enter a username: ".center(80),
                   run.COLORS['BLUE'],
                   attrs=['bold'])
            player = input()
            if validate_player_name(player):
                if player not in USERNAME.col_values(1):
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        f"Hello {player} ...you are player 2 "
                        f"({run.PLAYER_2} )..."
                        .center(80),
                        run.COLORS['YELLOW'],
                        attrs=['bold'])
                    vis.blank_line()
                    loading = ".....Loading.....".center(80)
                    vis.typing_text(loading)
                    # Converts the player input into an list item
                    # so it can be handled in google sheets
                    player2_username = player.split()
                    USERNAME.append_row(player2_username)
                else:
                    run.cls()
                    vis.connect4_title()
                    cprint('Username not available please pick another'.center(
                        80),
                           run.COLORS['RED'],
                           attrs=['bold'])
                    continue
            else:
                continue
        return player


def player_login(player_number):
    """
    This function takes the player number parameter
    If player number is equal to 0 player 1 inputs username
    It checks if that username is already in google sheets
    and if not throws and error, if so it returns player_username
    Does the same thing for player 2 if player number is = 1
    Player 2's input also has to be checked
    Against the returned player 1 username
    So the same name cant be used twice to log in
    """
    while True:
        if player_number == 0:
            # Player 1 inputs username
            cprint("Player 1 please log in with your username: ".center(80),
                   run.COLORS['BLUE'],
                   attrs=['bold'])
            player_username = input()
            if player_username in USERNAME.col_values(1):
                run.cls()
                vis.connect4_title()
                cprint(
                    f'Welcome back {player_username}. You are Player 1 '
                    f'({run.PLAYER_1} )'
                    .center(80),
                    run.COLORS['RED'],
                    attrs=['bold'])
                vis.blank_line()

                return player_username
            else:
                run.cls()
                vis.connect4_title()
                cprint('Cannot find username \n'.center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                continue
        else:
            # Player 2 inputs username
            cprint("Player 2 please log in with your username: ".center(80),
                   run.COLORS['BLUE'],
                   attrs=['bold'])
            player_username = input()
            if player_username in USERNAME.col_values(1):
                if player_username != player_one:
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        f'Welcome back {player_username}. You are Player 2 '
                        f'({run.PLAYER_2} )'
                        .center(80),
                        run.COLORS['YELLOW'],
                        attrs=['bold'])
                    vis.blank_line()
                    return player_username
                else:
                    run.cls()
                    vis.connect4_title()
                    cprint(
                        'Cannot choose a username thats already logged in \n'.
                        center(80),
                        run.COLORS['RED'],
                        attrs=['bold'])
            else:
                run.cls()
                vis.connect4_title()
                cprint('Cannot find username \n'.center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                continue


def validate_player_name(player):
    """
    This functions checks the player_name(players username input)
    It makes sure that the player_name is between 3 and 10 characters long
    If it doesn't fulfil this criteria it prints out an error message
    """
    try:
        if len(player) < 3 or len(player) > 10:
            vis.connect4_title()
            vis.blank_line()
            cprint(
                'Username must be between 3 and 10 characters long'.center(80),
                run.COLORS['RED'],
                attrs=['bold'])
        else:
            return True
    except TypeError:
        return False


def get_user_one():
    """
    Allows the player 1 user to create a username or login
    Calls the appropriate functions depending on the user input
    1 to create username - create_username()
    2 to Log In - player_login()
    Stores the players input in a variable called player_one
    """
    global player_one
    global player1_wins
    global player1_total_wins
    global player1_losses
    global player1_total_losses
    global player1_data

    player1_total_losses = 0
    player1_total_wins = 0
    player1_wins = 0
    player1_losses = 0

    while True:
        # Player 1 create username/login
        cprint('Player 1\n '.center(80), run.COLORS['RED'], attrs=['bold'])
        cprint('Press 1) Create username\n '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        cprint('Press 2) Login '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        menu_choice = input()
        if menu_choice == '1':
            run.cls()
            vis.connect4_title()
            player_one = create_username(PLAYERS[0], 0)
            # Sets the player spreadsheet coordinates
            # To be used later to update player scores
            player1_data = USERNAME.find(player_one).row
            # Set the base values of 0 for new players
            # For total wins and losses
            USERNAME.update_cell(player1_data, 2, '0')
            USERNAME.update_cell(player1_data, 3, '0')
            player1_total_wins = int(USERNAME.row_values(player1_data)[1])
            player1_total_losses = int(USERNAME.row_values(player1_data)[2])

            return player_one, player1_data, player1_total_losses,
            player1_total_wins

        elif menu_choice == '2':
            run.cls()
            vis.connect4_title()
            player_one = None
            player_one = player_login(0)
            loading = ".....Loading.....".center(80)
            vis.typing_text(loading)
            player1_data = USERNAME.find(player_one).row
            player1_total_wins = int(USERNAME.row_values(player1_data)[1])
            player1_total_losses = int(USERNAME.row_values(player1_data)[2])

            return player_one, player1_total_wins, player1_total_losses

        else:
            if menu_choice != '1' or '2':
                run.cls()
                vis.connect4_title()
                cprint('Please press 1 or 2 to make your choice'.center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                vis.blank_line()
                continue


def get_user_two():
    """
    Allows the player 2 user to create a username or login
    Calls the appropriate functions depending on the user input
    1 to create username - create_username()
    2 to Log In - player_login()
    Stores the players input in a variable called player_two
    """
    global player_two
    global player2_wins
    global player2_total_wins
    global player2_losses
    global player2_total_losses
    global player2_data

    player2_total_wins = 0
    player2_total_losses = 0
    player2_wins = 0
    player2_losses = 0

    while True:
        # Player 2 create username/login
        cprint('Player 2\n '.center(80), run.COLORS['YELLOW'], attrs=['bold'])
        cprint('Press 1) Create username\n '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        cprint('Press 2) Login '.center(80),
               run.COLORS['BLUE'],
               attrs=['bold'])
        menu_choice = input()
        if menu_choice == '1':
            run.cls()
            vis.connect4_title()
            player_two = create_username(PLAYERS[1], 1)
            # Sets the player spreadsheet coordinates
            # To be used later to update player scores
            player2_data = USERNAME.find(player_two).row
            USERNAME.update_cell(player2_data, 2, '0')
            USERNAME.update_cell(player2_data, 3, '0')
            player2_total_wins = int(USERNAME.row_values(player2_data)[1])
            player2_total_losses = int(USERNAME.row_values(player2_data)[2])

            return player_two, player2_data, player2_total_losses,
            player2_total_wins

        elif menu_choice == '2':
            run.cls()
            vis.connect4_title()
            player_two = player_login(1)
            loading = ".....Loading.....".center(80)
            vis.typing_text(loading)
            player2_data = USERNAME.find(player_two).row
            player2_total_wins = int(USERNAME.row_values(player2_data)[1])
            player2_total_losses = int(USERNAME.row_values(player2_data)[2])

            return player_two, player2_total_wins, player2_total_losses
        else:
            if menu_choice != '1' or '2':
                run.cls()
                vis.connect4_title()
                cprint('Please press 1 or 2 to make your choice'.center(80),
                       run.COLORS['RED'],
                       attrs=['bold'])
                vis.blank_line()
                continue


def cont_error(cont_input):
    """
    Function for error handling
    Press C to continue
    Making sure only C or c can be pressed
    """
    while cont_input not in ['c', 'C']:
        cprint('Please press C to continue...'.center(80),
               run.COLORS['RED'],
               attrs=['bold'])
        cont_input = input()
