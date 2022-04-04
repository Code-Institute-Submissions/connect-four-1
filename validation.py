import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('connect4')

USERNAME = SHEET.worksheet('usernames')
data = USERNAME.get_all_values()
FIRST_PLAYER = 0
SECOND_PLAYER = 1

class Users():
    """
    This Function will create a user object
    """
    def __init__(self, username):
        self.username = username
        
    

    def get_user_name(self):
        """
        """
        
        while True:
            if self.username == 0:
                player_name = input(" Player 1 please enter a username: ")
                if validate_player_name(player_name):
                    if player_name not in USERNAME.col_values(1):
                        player1_username = player_name.split()
                        USERNAME.append_row(player1_username)
                        print(' ')
                        print(f" Hello {player_name} ...you are player 1...")
                        print(' ')
                    else:
                        print(' ')
                        print(' Username not available please pick another')
                        print(' ')
                        continue
                else:
                    continue   
            else:
                player_name = input(" Player 2 please enter a username: ")
                if validate_player_name(player_name):
                    if player_name not in USERNAME.col_values(1):
                        player2_username = player_name.split()
                        USERNAME.append_row(player2_username)
                        print(' ')
                        print(f" Hello {player_name} ...you are player 2 ...caluclating next move...")
                        print(' ')  
                    else:
                        print(' ')
                        print('Username not available please pick another')
                        print(' ')
                        continue
                else:
                    continue
            return player_name
                             
def validate_player_name(player):
    try:
        if len(player) < 3 or len(player) > 10:
            print('Username must be between 3 and 10 characters long')

        else:
            return True

    except TypeError:
        return False

user_one = Users(FIRST_PLAYER)
user_one.get_user_name()
user_two = Users(SECOND_PLAYER)
user_two.get_user_name()

    
