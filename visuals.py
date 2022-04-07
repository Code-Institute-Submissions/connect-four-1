from pyfiglet import figlet_format
import colorama
from termcolor import cprint
import run as run
import validation as val

colorama.init(autoreset=True)


def blank_line():
    """
    Function to print off a blank line
    """
    print(' ')


def connect4_title():
    """
    Function to print off the connect 4 title
    """
    color = 'yellow'
    cprint(figlet_format(' Connect            4 !         ',
                         font="banner3-D",
                         justify='center'),
           color,
           attrs=['bold'])


def game_bar():
    """
    Function which creates a game bar displaying player info
    Using cprint statements
    """
    blank_line()
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    cprint(
        f'Player 1 : {val.player_one}                Player 2 : {val.player_two}'
        .center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
    cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])


def game_over_text(player):
    """
    Function which creates a game-over bar
    Displays the winner of the game
    Takes the player parameter
    """
    if player == 0:
        blank_line()
        cprint(f'PLAYER 1 ({val.player_one}) WINS! \n'.center(80),
               run.COLORS['WHITE'], run.COLORS['RED_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['RED_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['RED_HL'])
    elif player == 1:
        blank_line()
        cprint(f'PLAYER 2 ({val.player_two}) WINS! \n'.center(80),
               run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['YELLOW_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['YELLOW_HL'])
    else:
        blank_line()
        cprint('NO WINNERS! \n'.center(80),
               run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])
        cprint('GAME OVER!'.center(80), run.COLORS['WHITE'],
               run.COLORS['YELLOW_HL'])
        cprint(' '.center(80), run.COLORS['WHITE'], run.COLORS['BLUE_HL'])