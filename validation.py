import gspread
from google.oauth2.service_account import Credentials
import run as run
import time
from pyfiglet import figlet_format

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Scope as defined in the Love Sandwiches walk through project by Code Institute
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
    It calls the validate_player_name function to check that the username fills the proper criteria
    It checks if the player_name input has already been added to out google sheets
    if so, it calls an error and prompting the user to pick a different username
    if not it adds the player_name input to the google sheets
    """
    while True:
        player1_username = None
        player2_username = None

        # Player One creates username
        if player_number == 0:
            player = input(" Player 1 please enter a username: ")
            if validate_player_name(player):
                if player not in USERNAME.col_values(1):
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(f" Hello {player} ...you are player 1...")
                    time.sleep(1.4)
                    # Converts the player input into an list item so it can be handled in google sheets
                    player1_username = player.split()
                    USERNAME.append_row(player1_username)
                    run.cls()
                else:
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(' Username not available please pick another')
                    print(' ')
                    continue
            else:
                continue
        else:
            # Player Two creates username
            player = input(" Player 2 please enter a username: ")
            if validate_player_name(player):
                if player not in USERNAME.col_values(1):
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(f" Hello {player} ...you are player 2 ...caluclating next move...")
                    # Converts the player input into an list item so it can be handled in google sheets
                    player2_username = player.split()
                    USERNAME.append_row(player2_username)
                else:
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(' Username not available please pick another')
                    print(' ')
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
    Player 2's input also has to be checked against the returned player 1 username
    So the same name cant be used twice to log in
    """
    while True:
        if player_number == 0:
            # Player 1 inputs username
            player_username = input(" Player 1 please enter your username: ")
            if player_username in USERNAME.col_values(1):
                run.cls()
                print(figlet_format(' Connect 4!', font = "banner"))
                print(f' Welcome back {player_username}. You are Player 1')
                time.sleep(1.4)
                run.cls()
                return player_username  
            else:
                run.cls()
                print(figlet_format(' Connect 4!', font = "banner"))
                print(' Cannot find username')
                print(' ')
                continue
        else:
            # Player 2 inputs username
            player_username = input(" Player 2 please enter a username: ")
            if player_username in USERNAME.col_values(1):
                if player_username != player_one:
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(f' Welcome back {player_username}. You are Player 2')
                    time.sleep(1.4)
                    return player_username
                else:
                    run.cls()
                    print(figlet_format(' Connect 4!', font = "banner"))
                    print(' Cannot choose a username thats already logged in')
                    print(' ')
            else:
                run.cls()
                print(figlet_format(' Connect 4!', font = "banner"))
                print(' Cannot find username')
                print(' ')
                continue


def validate_player_name(player):
    """
    This functions checks the player_name(players username input)
    It makes sure that the player_name is between 3 and 10 characters long
    If it doesn't fulfil this criteria it prints out an error message
    """
    try:
        if len(player) < 3 or len(player) > 10:
            print(figlet_format(' Connect 4!', font = "banner"))
            print(' ')
            print(' Username must be between 3 and 10 characters long')
        else:
            return True
    except TypeError:
        return False


def get_users():
    """
    This function calls on the create_username function
    And the log_in function
    To give Player 1 and Player 2 options
    To either create a username or log in
    It also validates the inputs
    Its returns the usernames for player 1 and player 2
    For the game
    """

    global player_one
    global player_two

    while True:
        # Player 1 create username/login
        menu_choice = input(' Player 1\n \n Press 1) Create username\n \n Press 2) Login')
        if menu_choice == '1':
            run.cls()
            print(figlet_format(' Connect 4!', font = "banner"))
            player_one = create_username(PLAYERS[0], 0)
        elif menu_choice == '2':
            run.cls()
            print(figlet_format(' Connect 4!', font = "banner"))
            player_one = None
            player_one = player_login(0)
        else:
            if menu_choice != '1' or '2':
                run.cls()
                print(figlet_format(' Connect 4!', font = "banner"))
                print(' Please press 1 or 2 to make your choice')
                print(' ')
                continue

        # Player 2 create username/login
        print(figlet_format(' Connect 4!', font = "banner"))
        menu_choice = input(' Player 2\n \n Press 1) Create username\n \n Press 2) Login')
        if menu_choice == '1':
            run.cls()
            print(figlet_format(' Connect 4!', font = "banner"))
            player_two = create_username(PLAYERS[1], 1)
        elif menu_choice == '2':
            run.cls()
            print(figlet_format(' Connect 4!', font = "banner"))
            player_two = player_login(1)
        else:
            if menu_choice != '1' or '2':
                run.cls()
                print(figlet_format(' Connect 4!', font = "banner"))
                print(' Please press 1 or 2 to make your choice')
                print(' ')
                continue
        return player_one, player_two

