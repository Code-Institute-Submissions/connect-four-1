import gspread
from google.oauth2.service_account import Credentials

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
FIRST_PLAYER = 0
SECOND_PLAYER = 1

class Users():
    """
    Creates the user object which takes the players number
    And depending on the number creates the player 1 username
    or players 2 username, validates users input when creating
    the username
    """
    def __init__(self, player):
        self.player = player
        
    
    def get_user_name(self):
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
            # Player One creates username
            if self.player == 0:
                print(' ')
                player_name = input(" Player 1 please enter a username: ")
                print(' ')
                if validate_player_name(player_name):
                    # Checks if the user input is already in google sheets database and if it isn't runs the code
                    if player_name not in USERNAME.col_values(1):
                        # Converts the player input into an list item so it can be handled in google sheets
                        player1_username = player_name.split()
                        #Adds the created username to the google sheets database
                        USERNAME.append_row(player1_username)
                        print(' ')
                        print(f" Hello {player_name} ...you are player 1...")
                        print(' ')
                    else:
                        # If the username is in the google sheets database it prints the below error
                        print(' ')
                        print(' Username not available please pick another')
                        print(' ')
                        # Continue keyword, continues the loop until the proper conditions are fulfilled
                        continue
                else:
                    continue
            else:
                # Player Two creates username
                print(' ')
                player_name = input(" Player 2 please enter a username: ")
                print(' ')
                if validate_player_name(player_name):
                    # Checks if the user input is already in google sheets database and if it isn't runs the code
                    if player_name not in USERNAME.col_values(1):
                        # Converts the player input into an list item so it can be handled in google sheets
                        player2_username = player_name.split()
                        # Adds the created username to the google sheets database
                        USERNAME.append_row(player2_username)
                        print(' ')
                        print(f" Hello {player_name} ...you are player 2 ...caluclating next move...")
                        print(' ')
                    else:
                        # If the username is in the google sheets database it prints the below error
                        print(' ')
                        print('Username not available please pick another')
                        print(' ')
                        # Continue keyword, continues the loop until the proper conditions are fulfilled
                        continue
                else:
                    continue
            return player_name


def validate_player_name(player):
    """
    This functions checks the player_name(players username input)
    It makes sure that the player_name is between 3 and 10 characters long
    If it doesn't fulfil this criteria it prints out an error message
    """
    try:
        if len(player) < 3 or len(player) > 10:
            print(' ')
            print('Username must be between 3 and 10 characters long')
            print(' ')

        else:
            return True

    except TypeError:
        return False


player_one = Users(FIRST_PLAYER)
player_one.get_user_name()
player_two = Users(SECOND_PLAYER)
player_two.get_user_name()
